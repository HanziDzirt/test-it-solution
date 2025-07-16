from django.shortcuts import render, redirect
from .models import Citation, Source
import random
from django.db.models import ExpressionWrapper, FloatField, F
from .forms import CitationForm, SourceForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        if 'like' in request.POST:
            citation = Citation.objects.get(id=request.POST['like'])
            citation.likes += 1
            citation.save()
        elif 'dislike' in request.POST:
            citation = Citation.objects.get(id=request.POST['dislike'])
            citation.dislikes += 1
            citation.save()
        return redirect('/')

    citations = Citation.objects.all()
    weights = [citation.weight for citation in citations]
    random_citation = random.choices(citations, weights=weights, k=1)[0]
    random_citation.views += 1
    random_citation.save()
    return render(request, 'main/home.html', {'title': 'Главная страница','citation': random_citation})


def top10(request):
    top_by_rating = Citation.objects.annotate(
        rating=ExpressionWrapper(
            (F('likes') + 1) / (F('dislikes') + 1),
            output_field=FloatField()
        )
    ).order_by('-rating')[:10]

    top_by_views = Citation.objects.order_by('-views')[:10]
    top_by_likes = Citation.objects.order_by('-likes')[:10]

    return render(request, 'main/top10.html', {
        'title': 'Топ цитат',
        'top_by_rating': top_by_rating,
        'top_by_views': top_by_views,
        'top_by_likes': top_by_likes
    })


def add(request):
    error = ''
    formC = CitationForm()
    formS = SourceForm()
    if request.method == 'POST':
        formC = CitationForm(request.POST)
        if formC.is_valid():
            text = formC.cleaned_data['text']
            source = formC.cleaned_data['source']
            if Citation.objects.filter(text=text).exists():
                messages.error(request, 'Цитата уже существует!')
            elif Citation.objects.filter(source=source).count() >= 3:
                messages.error(request, 'У источника максимум 3 цитаты!')
            else:
                formC.save()
                messages.success(request, 'Цитата добавлена!')

        else:
            error = 'Что-то пошло не так'

        formS = SourceForm(request.POST)
        if formS.is_valid():
            name = formS.cleaned_data['name']
            if Source.objects.filter(name=name, type=type).exists():
                messages.error(request, 'Источник уже существует!')
            else:
                formS.save()
                messages.success(request, 'Источник добавлен!')
        else:
            error = 'Что-то пошло не так'

    context = {
        'formC': formC,
        'formS': formS,
        'error': error,
        'title': 'Добавление цитаты',
    }
    return render(request, 'main/add.html', context)
