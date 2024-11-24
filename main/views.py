from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'China - Главная',
        'content': 'Онлайн магазин товаров из Китая',
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'China - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о крутизне данного магаза'
    }

    return render(request, 'main/about.html', context)




