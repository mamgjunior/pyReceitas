from django.urls import path
from .import views

app_name = 'receitas'

urlpatterns = [
    path('', views.index, name='index'),
    path('receita/<int:pk>/', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar'),
]