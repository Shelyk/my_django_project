from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .forms import SigUpForm
from .models import MenuItem, Post
from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()
        posts = Post.objects.all()
        paginator = Paginator(posts, 6)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'main/home.html', context={
            "menu_items": menu_items,
            'page_obj': page_obj
        })


class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        return render(request, 'main/post_detail.html', context={
            'post': post
    })

def contact(request):
    return render(request, "main/contact.html")

def sign_up(request):
    if request.method == "POST":
        user = User()
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.set_password(request.POST.get("password"))
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.save()
        if user:
            login(request, user)
        return redirect("/")
    else:
        return render(request, "main/sign-up.html", {})

# class SignUpView(View):
#     def get(self, request, *args, **kwargs):
#         form = SigUpForm()
#         return render(request, 'myblog/signup.html', context={
#             'form': form,
#         })
#     def post(self, request, *args, **kwargs):
#         form = SigUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#         return render(request, 'myblog/signup.html', context={
#             'form': form,
#         })

def sign_in(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        print("================USER ===============")
        print(user)
        if user:
            login(request, user)
        return redirect("/")
    else:
        return render(request, "main/sign-in.html", {})



def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")