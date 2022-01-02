from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),    
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('criar/receita/', views.criar_receita, name='criar_receita'),
]
