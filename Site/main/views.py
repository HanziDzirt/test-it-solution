from django.shortcuts import render, redirect
from .forms import CitationForm
from .models import Citation
import random
from django.db.models import ExpressionWrapper, FloatField, F
from .forms import CitationForm, SourceForm

def home(request):
    citations = Citation.objects.all()
    weights = [citation.weight for citation in citations]
    random_citation = random.choices(citations, weights=weights, k=1)[0]
    random_citation.views += 1
    random_citation.save()
    return render(request, 'main/home.html', {'title': 'Главная страница','citation': random_citation})

def top10(request):
    top_list = Citation.objects.annotate(
        rating=ExpressionWrapper(
            F('likes') / (F('likes') + F('dislikes') + 1),  # Здесь была незакрытая скобка
            output_field=FloatField()
        )
    ).order_by('-rating')[:10]
    return render(request, 'main/top10.html', {'title': 'Десять лучших цитат', 'citations': top_list})

def add(request):
    error = ''
    if request.method == 'POST':
        formC = CitationForm(request.POST)
        if form.is_valid():
            form.save()
        formS = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'ERROR'
    formC = CitationForm()
    formS = SourceForm()
    context = {
        'formC': formC,
        'formS': formS,
        'error': error,
    }
    return render(request, 'main/add.html',{'title': 'Добавление цитаты'})