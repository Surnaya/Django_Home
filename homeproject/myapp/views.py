from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django сайт!</h1>
    <p>Здесь пока ничего нет .....</p>
    """
    return HttpResponse(html)


def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Привет! Меня зовут Рита. Это мой первый проект на Django.</p>
    """
    return HttpResponse(html)
