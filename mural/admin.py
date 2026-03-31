from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoria, Aviso


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'categoria', 'data_criacao')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('categoria', 'data_criacao')
    ordering = ('-data_criacao',)