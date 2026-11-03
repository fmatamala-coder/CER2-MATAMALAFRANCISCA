from django.contrib import admin
from .models import Categoria, LugarPatrimonial

# Register your models here.
#admin.site.register(Categoria)
#admin.site.register(LugarPatrimonial)

# Anotación
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    
@admin.register(LugarPatrimonial)
class LugarPatrimonialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'ubicacion', 'anio_construccion')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'ubicacion')