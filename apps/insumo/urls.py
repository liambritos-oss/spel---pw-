from django.urls import path
from .views import InsumoListView, InsumoCreateView, InsumoUpdateView, InsumoDeleteView, InsumoDetailView

app_name= 'insumo'

urlpatterns = [
    path('', InsumoListView.as_view(), name='insumo_list'),
    path('create/', InsumoCreateView.as_view(), name='insumo_create'),
    path('<int:pk>/update/', InsumoUpdateView.as_view(), name='insumo_update'),
    path('<int:pk>/delete/', InsumoDeleteView.as_view(), name='insumo_delete'),
    path('<int:pk>/', InsumoDetailView.as_view(), name='insumo_detail'),
]