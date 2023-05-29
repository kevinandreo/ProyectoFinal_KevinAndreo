from django.test import TestCase
from django.contrib.auth.models import User
from .models import Articulo

class ArticuloTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.articulo = Articulo.objects.create(
            titulo='Título de prueba',
            subtitulo='Subtítulo de prueba',
            cuerpo='Cuerpo de prueba',
            autor=self.user
        )

    def test_articulo_str(self):
        self.assertEqual(str(self.articulo), 'Título de prueba')

    def test_articulo_autor(self):
        self.assertEqual(self.articulo.autor, self.user)



