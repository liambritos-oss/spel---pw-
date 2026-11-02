from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

class InicioView(PermissionRequiredMixin, TemplateView):
    template_name = 'inicio/inicio.html'