from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Articulo
from .forms import ArticuloForm

class HomeView(View):
    def get(self, request):
        return render(request, 'blog/home.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'blog/about.html')

class ListaArticulosView(View):
    def get(self, request):
        articulos = Articulo.objects.all()
        return render(request, 'blog/lista_articulos.html', {'articulos': articulos})

class DetalleArticuloView(View):
    def get(self, request, articulo_id):
        articulo = get_object_or_404(Articulo, pk=articulo_id)
        return render(request, 'blog/detalle_articulo.html', {'articulo': articulo})

@method_decorator(login_required, name='dispatch')
class CrearArticuloView(View):
    def get(self, request):
        form = ArticuloForm()
        form.fields['autor'].queryset = User.objects.filter(username=request.user.username)
        return render(request, 'blog/crear_articulo.html', {'form': form})

    def post(self, request):
        form = ArticuloForm(request.POST, request.FILES)
        form.fields['autor'].queryset = User.objects.filter(username=request.user.username)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            return redirect('blog:lista_articulos')
        return render(request, 'blog/crear_articulo.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class EditarArticuloView(View):
    def get(self, request, articulo_id):
        articulo = get_object_or_404(Articulo, pk=articulo_id)
        form = ArticuloForm(instance=articulo)
        form.fields['autor'].queryset = User.objects.all()
        return render(request, 'blog/editar_articulo.html', {'form': form, 'articulo': articulo})

    def post(self, request, articulo_id):
        articulo = get_object_or_404(Articulo, pk=articulo_id)
        form = ArticuloForm(request.POST, instance=articulo)
        form.fields['autor'].queryset = User.objects.all()
        if form.is_valid():
            articulo_autor_anterior = articulo.autor
            form.save()
            articulo = form.instance
            articulo.autor = articulo_autor_anterior
            articulo.save()
            return redirect('blog:detalle_articulo', articulo_id=articulo_id)
        return render(request, 'blog/editar_articulo.html', {'form': form, 'articulo': articulo})

@method_decorator(login_required, name='dispatch')
class EliminarArticuloView(View):
    def get(self, request, articulo_id):
        articulo = get_object_or_404(Articulo, pk=articulo_id)
        return render(request, 'blog/eliminar_articulo.html', {'articulo': articulo})

    def post(self, request, articulo_id):
        articulo = get_object_or_404(Articulo, pk=articulo_id)
        articulo.delete()
        return redirect('blog:lista_articulos')


