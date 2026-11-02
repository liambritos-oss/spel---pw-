from django.shortcuts import render
from .models import Publicacion
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin

class PublicacionListView(PermissionRequiredMixin, ListView):
    model = Publicacion
    template_name = 'publicacion/list.html'
    success_url = reverse_lazy('publicacion:publicacion_list')

class PublicacionCreateView(PermissionRequiredMixin, CreateView):
    model = Publicacion
    template_name = 'publicacion/create.html'
    fields = "__all__"
    success_url = reverse_lazy('publicacion:publicacion_list')

class PublicacionUpdateView(PermissionRequiredMixin, UpdateView):
    model = Publicacion
    template_name = 'publicacion/update.html'
    fields = "__all__"
    success_url = reverse_lazy('publicacion:publicacion_list')

class PublicacionDeleteView(PermissionRequiredMixin, DeleteView):
    model = Publicacion
    template_name = 'publicacion/delete.html'
    success_url = reverse_lazy('publicacion:publicacion_list')

class PublicacionDetailView(PermissionRequiredMixin, DetailView):
    model = Publicacion
    template_name = 'publicacion/detalle.html'
    context_object_name = "publicacion"