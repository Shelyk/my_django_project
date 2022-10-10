from django.shortcuts import render, redirect, get_object_or_404
from .models import News, Category


def news_site(request):
    news = News.objects.filter(display_on_main_page=True, approved=True).order_by('-id')
    return render(request, "news/news.html", {"news": news})


def add_news(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "news/add.html")
        else:
            news = News()
            news.title = request.POST.get('title')
            news.description = request.POST.get('description')
            news.user = request.user
            news.save()
            return redirect("/")
    else:
        redirect("/")


def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news/detail.html', {'news': news})


def categories_site(request):
    category = Category.objects.all()
    return render(request, "news/categories.html", {"category": category})