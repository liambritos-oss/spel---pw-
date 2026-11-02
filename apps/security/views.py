from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

class SecurityView(LoginRequiredMixin, LoginView):
    template_name = 'security/login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    pass