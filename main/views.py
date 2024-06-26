from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        'title': 'MatroSkin - Главная',
        'content': "MatroSkin",
    }

    return render(request, 'main/index.html', context)
    

def about(request):
    context = {
        'title': 'MatroSkin - О нас',
        'content': "О нас",
        'text_on_page': "Мы бренд одежды MatroSkin. Изготавливаем вышивку."
    }

    return render(request, 'main/about.html', context)