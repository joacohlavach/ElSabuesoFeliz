from django.db import models

# Create your models here.
    
class Raza(models.Model):
    denominacion = models.CharField(max_length=100)
    pesoMinimoMachos = models.FloatField()
    pesoMaximoMachos = models.FloatField()
    pesoMinimoHembras = models.FloatField()
    pesoMaximoHembras = models.FloatField()
    alturaMediaMachos = models.FloatField()
    alturaMediaHembras = models.FloatField()
    cuidadosEspeciales = models.TextField()

    def __str__(self):
        return self.denominacion
    
class Duenio(models.Model):
    apellido = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.apellido}, {self.nombres}"
class Perro(models.Model):
    numeroHistoriaClinica = models.IntegerField()
    nombre = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    pesoActual = models.FloatField()
    alturaActual = models.FloatField()
    duenio = models.ForeignKey(Duenio, on_delete=models.CASCADE)
    consulta = models.TextField()
    vacuna = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

    