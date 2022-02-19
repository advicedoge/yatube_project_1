from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    title = 'Yatube Главная страница'
    context = {
        'title': title,
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)


def group_posts(request, slug):
    title = 'Страница сообщества Yatube'
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube'
    }

    return render(request, context)
