from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import News, Categories


def index(request):
    news = News.objects.all()
    context = {'news': news, 'title': 'Список новостей'}
    return render(request=request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Categories.objects.get(pk=category_id)
    categories = Categories.objects.all()
    return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category})


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})
