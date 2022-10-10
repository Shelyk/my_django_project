from django.urls import path
from .views import news_site, categories_site, add_news, news_detail

urlpatterns = [
    path("/", news_site, name="news"),
    path("/add", add_news, name="add_news"),
    path("/<int:id>", news_detail, name="news_detail"),
    path("/category/", categories_site, name="category")
]