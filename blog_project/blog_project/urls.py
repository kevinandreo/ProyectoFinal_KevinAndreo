"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import include, path, re_path
from blog.views import HomeView, AboutView, ListaArticulosView, DetalleArticuloView, CrearArticuloView, EditarArticuloView, EliminarArticuloView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('perfiles/', include('perfiles.urls', namespace='perfiles')),
    path('', HomeView.as_view(), name='blog_home'),
    path('about/', AboutView.as_view(), name='blog_about'),
    path('articulos/', ListaArticulosView.as_view(), name='blog_lista_articulos'),
    path('articulos/<int:articulo_id>/', DetalleArticuloView.as_view(), name='blog_detalle_articulo'),
    path('articulos/crear/', CrearArticuloView.as_view(), name='blog_crear_articulo'),
    path('articulos/editar/<int:articulo_id>/', EditarArticuloView.as_view(), name='blog_editar_articulo'),
    path('articulos/eliminar/<int:articulo_id>/', EliminarArticuloView.as_view(), name='blog_eliminar_articulo'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]