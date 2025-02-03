from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,FormView
from .form import UserResgtrationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.
class HomePageView(TemplateView):
    template_name ="my_app/home.html"


class AboutPageView(TemplateView):
    template_name ="my_app/about.html"


class UserResgtrationView(CreateView):
    form_class = UserResgtrationForm
    template_name = "my_app/register.html"
    success_url = reverse_lazy("home")

class UserLoginView(FormView):
    form_class = AuthenticationForm
    template_name ="my_app/login.html"
    success_url = reverse_lazy("home")
    def form_valid(self,form):
        if form.cleaned_data.get("username") and form.cleaned_data.get("password"):
            user = form.get_user()
            if user:
                login(self.request,user)
        else:
            return self.form_invalid(form)  # Treat as invalid if empty data is present
        return super().form_valid(form)