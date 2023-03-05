from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model):

    surname = models.TextField(max_length=300),
   


class Actividad(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=300)
    info= models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
   

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['completo']