from django.db import models
import datetime

class Post(models.Model):
    titulo = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    contenido = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)