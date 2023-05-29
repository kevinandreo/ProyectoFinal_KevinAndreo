from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegistroForm, PerfilForm
from django.contrib.auth.mixins import LoginRequiredMixin

class RegistroView(View):
    def get(self, request):
        form = RegistroForm()
        perfil_form = PerfilForm()
        return render(request, 'perfiles/registro.html', {'form': form, 'perfil_form': perfil_form})

    def post(self, request):
        form = RegistroForm(request.POST)
        perfil_form = PerfilForm(request.POST)
        if form.is_valid() and perfil_form.is_valid():
            user = form.save()
            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()
            login(request, user)
            return redirect('blog:lista_articulos')
        else:
            print(form.errors)
            print(perfil_form.errors)
        return render(request, 'perfiles/registro.html', {'form': form, 'perfil_form': perfil_form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'perfiles/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:lista_articulos')
        return render(request, 'perfiles/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('blog:home')

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        perfil = user.perfil
        return render(request, 'perfiles/profile.html', {'user': user, 'perfil': perfil})