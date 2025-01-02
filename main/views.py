from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import first

def index(request):
    context = {
        'title': 'home',
        'content': 'Главная страница',
        'list': ['first', 'two'],
        'dict': {'three': 'one'},
        'is_authenticated': True
    }
    
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')