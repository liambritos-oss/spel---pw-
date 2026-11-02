from django.urls import path
from .views import PublicacionListView, PublicacionCreateView, PublicacionUpdateView, PublicacionDeleteView, PublicacionDetailView

app_name = 'publicacion'

urlpatterns = [
    path('', PublicacionListView.as_view(), name='publicacion_list'),
    path('create/', PublicacionCreateView.as_view(), name='publicacion_create'),
    path('<int:pk>/update/', PublicacionUpdateView.as_view(), name='publicacion_update'),
    path('<int:pk>/delete/', PublicacionDeleteView.as_view(), name='publicacion_delete'),
    path('<int:pk>/', PublicacionDetailView.as_view(), name='publicacion_detail'),
]