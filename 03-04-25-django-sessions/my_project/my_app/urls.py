from django.urls import path
from .views import HomePageView,AboutPageView,UserResgtrationView,UserLoginView,UserLogoutView


urlpatterns =[
    path("",HomePageView.as_view(),name="home"),
    path("about/",AboutPageView.as_view(),name="about"),
    path("register/",UserResgtrationView.as_view(),name="register"),
    path("login/",UserLoginView.as_view(),name="login"),
    path("logout",UserLogoutView.as_view(),name="logout")
]