from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class LugarPatrimonial(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    ubicacion = models.CharField(max_length=150, blank=True, null=True)
    anio_construccion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)])
    imagen = models.URLField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    