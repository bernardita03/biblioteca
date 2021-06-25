from django.db import models

class Solicitud(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    año = models.IntegerField()

    def __str__(self):
        return self.titulo