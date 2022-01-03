from django.urls import path
from . views import *

app_name = 'receitas'

urlpatterns = [
    path('', index, name='index'),
    path('buscar', buscar, name='buscar'),
    path('receita/<int:pk>/', receita, name='receita'),    
    path('criar/receita/', criar_receita, name='criar_receita'),
    path('editar/<int:pk>', editar_receita, name='editar_receita'),
    path('deletar/<int:pk>', deletar_receita, name='deletar_receita'),    
    path('atualizar_receita/', atualizar_receita, name='atualizar_receita'),
]