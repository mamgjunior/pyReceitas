from django.contrib import admin
from . models import Receita

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_receita', 'categoria', 'tempo_preparo', 'date_receita', 'publicada']
    list_display_links = ['id', 'nome_receita']
    search_fields = ('nome_receita', )
    list_filter = ('categoria', )
    list_editable = ('publicada', )
    list_per_page = 2
