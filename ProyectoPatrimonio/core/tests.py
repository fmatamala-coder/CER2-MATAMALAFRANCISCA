from django.test import TestCase
from django.urls import reverse

from .models import Categoria, LugarPatrimonial


class DetalleLugarTests(TestCase):
    def test_detalle_muestra_la_url_de_imagen_guardada(self):
        categoria = Categoria.objects.create(nombre="Monumentos")
        lugar = LugarPatrimonial.objects.create(
            categoria=categoria,
            nombre="Edificio Histórico",
            anio_construccion=1900,
            imagen="https://example.com/edificio.jpg",
        )

        response = self.client.get(reverse("core:detalle_lugar", args=[lugar.id]))

        self.assertContains(response, '<img src="https://example.com/edificio.jpg"')
