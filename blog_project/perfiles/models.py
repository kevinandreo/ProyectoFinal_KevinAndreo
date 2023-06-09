from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(default='')
    website = models.URLField(default='')

    def __str__(self):
        return self.user.username
