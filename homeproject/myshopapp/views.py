from django.shortcuts import render

from django.http import HttpResponse


def shop(request):
    html = """
    <h1>Добро пожаловать в магазин!</h1>
    <p>Здесь пока ничего нет .....</p>
    """
    return HttpResponse(html)
