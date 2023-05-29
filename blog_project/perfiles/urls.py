from django.urls import path
from .views import RegistroView, LoginView, LogoutView
from perfiles.views import ProfileView
app_name = 'perfiles'

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]