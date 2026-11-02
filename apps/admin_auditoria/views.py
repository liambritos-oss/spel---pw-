from django.shortcuts import render
from .models import AdminAuditoria
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin

class AdminAuditoriaListView(PermissionRequiredMixin,ListView):
    model = AdminAuditoria
    template_name = 'admin_auditoria/list.html'
    success_url = reverse_lazy('')

class AdminAuditoriaCreateView(PermissionRequiredMixin,CreateView):
    model = AdminAuditoria
    template_name = 'admin_auditoria/create.html'
    fields = "__all__"
    success_url = reverse_lazy('admin_auditoria:admin_auditoria_list')

class AdminAuditoriaUpdateView(PermissionRequiredMixin,UpdateView):
    model = AdminAuditoria
    template_name = 'admin_auditoria/update.html'
    fields = "__all__"
    success_url = reverse_lazy('admin_auditoria:admin_auditoria_list')

class AdminAuditoriaDeleteView(PermissionRequiredMixin,DeleteView):
    model = AdminAuditoria
    template_name = 'admin_auditoria/delete.html'
    success_url = reverse_lazy('admin_auditoria:admin_auditoria_list')

class AdminAuditoriaDetailView(PermissionRequiredMixin,DetailView):
    model = AdminAuditoria
    template_name = "admin_auditoria/detalle.html"
    context_object_name = "admin_auditoria"