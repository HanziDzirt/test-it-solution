from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'main/home.html')
def top10(request):
    return render(request, 'main/top10.html')
def add(request):
    return render(request, 'main/add.html')