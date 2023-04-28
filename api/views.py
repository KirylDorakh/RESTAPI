import json
from django.http import HttpResponse
from django.shortcuts import render

from .models import Article


def get_article(_, pk):
    article = Article.objects.get(id=pk)
    return HttpResponse(content=article, status=200)


def get_articles(_):
    articles = Article.objects.all()
    return HttpResponse(content=articles, status=200)


def create_article(request):
    # достаем тело запроса. Тело закодировано. используем json для работы с ним как с dict
    body = json.loads((request.body.decode('utf-8')))
    article = Article.objects.create(
        title=body['title'],
        pages=body['pages']
    )
    return HttpResponse(content=article, status=201)


def edit_article(request, pk):
    body = json.loads((request.body.decode('utf-8')))
    article = Article.objects.get(id=pk)
    for attr, value in body.items():
        setattr(article, attr, value)
    article.save()
    return HttpResponse(content=article, status=200)


def delete_article(_, pk):
    article = Article.objects.get(id=pk).delete()
    return HttpResponse(status=204)
