from django.urls import path
from .views import MainView, \
    SignUpView, \
    SignInView, \
    contact, \
    PostDetailView, \
    SuccessView, \
    SearchResultsView, \
    TagView
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path("",  MainView.as_view(), name="home"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout',),
    path("contact", contact, name="contact"),
    path('contact/success/', SuccessView.as_view(), name='success'),
    path('post/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('tag/<slug:slug>/', TagView.as_view(), name="tag"),
]