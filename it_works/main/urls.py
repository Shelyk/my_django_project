from django.urls import path
from .views import MainView, sign_up, sign_in, logout_view, contact, PostDetailView

urlpatterns = [
    path("",  MainView.as_view(), name="home"),
    path("sign-up", sign_up, name="sign-up"),
    path("sign-in", sign_in, name="sign-in"),
    path("logout", logout_view, name="logout"),
    path("contact", contact, name="contact"),
    path('post/<slug>/', PostDetailView.as_view(), name='post_detail'),
]