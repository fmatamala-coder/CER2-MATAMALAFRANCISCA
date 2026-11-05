from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, LugarPatrimonial
from django.contrib.auth.decorators import login_required

# Create your views here.
# VISTA BASADA EN FUNCIONES (FBV)
def home(request):
    lugares = LugarPatrimonial.objects.all().order_by('-id')[:3]
    categorias = Categoria.objects.all()
    
    data = {
        'lugares_recientes': lugares,
        'categorias': categorias
    }
    return render(request, 'core/home.html', data)

def catalogo_lugares(request, categoria_id=None):
    categorias = Categoria.objects.all()
    
    # SI recibe un ID de categoría, filtramos; si no, mostramos
    if categoria_id:
        categoria_seleccionada = get_object_or_404(Categoria, id=categoria_id)
        lugares = LugarPatrimonial.objects.filter(categoria=categoria_seleccionada)
    else:
        categoria_seleccionada = None
        lugares = LugarPatrimonial.objects.all()
        
    data = {
        'categorias': categorias,
        'lugares': lugares,
        'categoria_seleccioanda': categoria_seleccionada
    }
    return render(request, 'core/catalogo.html', data)

def detalle_lugar(request, lugar_id):
    lugar = get_object_or_404(LugarPatrimonial, id=lugar_id)
    
    data = {
        'lugar': lugar
    }
    return render(request, 'core/detalle.html', data)

@login_required(login_url='/admin/login/')
def seccion_gestion(request):
    # Si el usuario ha iniciado sesión, lo mandamos directo al panel admin
    return redirect('/admin/')