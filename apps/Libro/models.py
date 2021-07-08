from django.db import models

# Create your models here.
CATEGORIAS = (
    ('Terror', 'Terror'),
    ('Ficcion', 'Ficcion'),
    ('Romance', 'Romance'),
    ('Literatura', 'Literatura'),
)

class Libro (models.Model):
    fotografia = models.ImageField(upload_to='libros')
    autor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=70)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return str(self.fotografia)