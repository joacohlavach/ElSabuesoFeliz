from django.db import models

# Create your models here.
class Veterinaria(models.Model):
    name = models.CharField(max_length=50)
    codigo_vet = models.IntegerField()

    def __str__(self):
        return self.name
    