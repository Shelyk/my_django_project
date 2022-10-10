from django.shortcuts import render, redirect

from .models import MenuItem


def home(request):
    menu_items = MenuItem.objects.all()
    return render(request, "main/home.html", {"menu_items": menu_items})
