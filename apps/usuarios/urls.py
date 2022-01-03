from django.urls import path
from .views import *

app_name = 'usuarios'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),    
    path('cadastro/', cadastro, name='cadastro'),
    path('dashboard/', dashboard, name='dashboard'),
]
