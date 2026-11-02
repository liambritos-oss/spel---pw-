from django.urls import path
from .views import AdminAuditoriaListView, AdminAuditoriaCreateView, AdminAuditoriaUpdateView, AdminAuditoriaDeleteView, AdminAuditoriaDetailView

app_name= 'admin_auditoria'

urlpatterns = [
    path('', AdminAuditoriaListView.as_view(), name='admin_auditoria_list'),
    path('create/', AdminAuditoriaCreateView.as_view(), name='admin_auditoria_create'),
    path('<int:pk>/update/', AdminAuditoriaUpdateView.as_view(), name='admin_auditoria_update'),
    path('<int:pk>/delete/', AdminAuditoriaDeleteView.as_view(), name='admin_auditoria_delete'),
    path('admin_auditorias/<int:pk>/',AdminAuditoriaDetailView.as_view(), name='admin_auditoria_detail'),
]