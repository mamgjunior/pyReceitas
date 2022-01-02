from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('receitas.urls', namespace='receitas')),
    path('admin/', admin.site.urls),    
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
