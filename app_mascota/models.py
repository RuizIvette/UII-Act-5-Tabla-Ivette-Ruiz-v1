from django.db import models

# Create your models here.

class Mascota(models.Model):
    nombre= models.CharField(max_length=100)
    edad= models.IntegerField()
    especie= models.CharField(max_length=100)

    def _str_(self):
        return f"{self.nombre}{self.especie}"