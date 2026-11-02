from django.shortcuts import render
from .models import Insumo
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
 
class InsumoListView(PermissionRequiredMixin, ListView):
    model = Insumo
    template_name = 'insumo/list.html'
    success_url = reverse_lazy('')

class InsumoCreateView(PermissionRequiredMixin, CreateView):
    model = Insumo
    template_name = 'insumo/create.html'
    fields = "__all__"
    success_url = reverse_lazy('insumo:insumo_list')

class InsumoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Insumo
    template_name = 'insumo/update.html'
    fields = "__all__"
    success_url = reverse_lazy('insumo:insumo_list')

class InsumoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Insumo
    template_name = 'insumo/delete.html'
    success_url = reverse_lazy('insumo:insumo_list')

class InsumoDetailView(PermissionRequiredMixin, DetailView):
    model = Insumo
    template_name = 'insumo/detalle.html'
    context_object_name = "insumo"