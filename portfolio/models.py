from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    activo = models.BooleanField(default=True)

class Projet(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = ImageField(upload_to="portfolio/image")
    url = URLField(blank=True)


