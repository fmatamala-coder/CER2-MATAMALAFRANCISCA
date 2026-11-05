from django.urls import path
from django.contrib import admin

from . import views

app_name = "core"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("catalogo/", views.catalogo_lugares, name="catalogo"),
    path(
        "catalogo/categoria/<int:categoria_id>/",
        views.catalogo_lugares,
        name="catalogo_por_categoria",
    ),
    path("lugar/<int:lugar_id>/", views.detalle_lugar, name="detalle_lugar"),
    
    path('gestion/', views.seccion_gestion, name='gestion'),
]
