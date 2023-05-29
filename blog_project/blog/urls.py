from django.urls import path
from .views import HomeView, AboutView, ListaArticulosView, DetalleArticuloView, CrearArticuloView, EditarArticuloView, EliminarArticuloView

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('articles/', ListaArticulosView.as_view(), name='lista_articulos'),
    path('articles/<int:articulo_id>/', DetalleArticuloView.as_view(), name='detalle_articulo'),
    path('articles/crear/', CrearArticuloView.as_view(), name='crear_articulo'),
    path('articles/editar/<int:articulo_id>/', EditarArticuloView.as_view(), name='editar_articulo'),
    path('articles/eliminar/<int:articulo_id>/', EliminarArticuloView.as_view(), name='eliminar_articulo'),
]