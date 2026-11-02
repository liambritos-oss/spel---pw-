from django.urls import path
from .views import DonacionesListView, DonacionesCreateView, DonacionesUpdateView, DonacionesDeleteView, DonacionesDetailView

app_name= 'donaciones'

urlpatterns = [
    path('', DonacionesListView.as_view(), name='donaciones_list'),
    path('create/', DonacionesCreateView.as_view(), name='donaciones_create'),
    path('<int:pk>/update/', DonacionesUpdateView.as_view(), name='donaciones_update'),
    path('<int:pk>/delete/', DonacionesDeleteView.as_view(), name='donaciones_delete'),
    path('donaciones/<int:pk>/',DonacionesDetailView.as_view(), name='donaciones_detail'),
]