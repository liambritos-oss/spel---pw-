from django.shortcuts import render
from .models import Donaciones
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin

class DonacionesListView(PermissionRequiredMixin, ListView):
    model = Donaciones
    template_name = 'donaciones/list.html'
    success_url = reverse_lazy('')

class DonacionesCreateView(PermissionRequiredMixin, CreateView):
    model = Donaciones
    template_name = 'donaciones/create.html'
    fields = "__all__"
    success_url = reverse_lazy('donaciones:donaciones_list')

class DonacionesUpdateView(PermissionRequiredMixin, UpdateView):
    model = Donaciones
    template_name = 'donaciones/update.html'
    fields = "__all__"
    success_url = reverse_lazy('donaciones:donaciones_list')

class DonacionesDeleteView(PermissionRequiredMixin, DeleteView):
    model = Donaciones
    template_name = 'donaciones/delete.html'
    success_url = reverse_lazy('donaciones:donaciones_list')

class DonacionesDetailView(PermissionRequiredMixin, DetailView):
    model = Donaciones
    template_name = 'donaciones/detalle.html'
    context_object_name = "donaciones"