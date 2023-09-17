from django.db import models

class Sucursal(models.Model):
    direccion = models.CharField(max_length=255)
    
    def __str__(self):
        return self.direccion

class Empleado(models.Model):
    numeroDocumento = models.IntegerField()
    nombres = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fechaNacimiento = models.DateField()
    fechaIngreso = models.DateField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombres} {self.apellido}"

class AsignacionEmpleados(models.Model):
    fechaIngreso = models.DateField()
    fechaEgreso = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion

class Perro(models.Model):
    numeroHistoriaClinica = models.IntegerField()
    nombre = models.CharField(max_length=255)
    fechaNacimiento = models.DateField()
    raza = models.ForeignKey('Raza', on_delete=models.CASCADE)
    pesoActual = models.FloatField()
    alturaActual = models.FloatField()
    historialMascotas = models.ForeignKey('HistorialMascotas', on_delete=models.CASCADE)
    consulta = models.TextField()
    vacuna = models.TextField()

    def __str__(self):
        return self.nombre

class HistorialMascotas(models.Model):
    estadoPerro = models.CharField(max_length=255)
    rolPersona = models.CharField(max_length=255)

    def __str__(self):
        return self.estadoPerro

class Persona(models.Model):
    nombrePersona = models.CharField(max_length=255)
    numDocPersona = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombrePersona

class Raza(models.Model):
    denominacion = models.CharField(max_length=255)
    pesoMinimoMachos = models.FloatField()
    pesoMaximoMachos = models.FloatField()
    pesoMinimoHembras = models.FloatField()
    pesoMaximoHembras = models.FloatField()
    alturaMediaMachos = models.FloatField()
    alturaMediaHembras = models.FloatField()
    cuidadosEspeciales = models.TextField()

    def __str__(self):
        return self.denominacion

class Consulta(models.Model):
    numeroOrden = models.IntegerField()
    fechaEntrada = models.DateField()
    sIntomas = models.TextField()
    diagnosticos = models.TextField()
    medicamento = models.TextField()
    fechaSalida = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)

    def __str__(self):
        return f"Consulta para {self.perro.nombre}"

class Vacunacion(models.Model):
    fechaProgramada = models.DateField()
    fechaReal = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion

class Vacuna(models.Model):
    nombreVacuna = models.CharField(max_length=255)
    empleado = models.CharField(max_length=255)
    laboratorio = models.CharField(max_length=255)
    dosis = models.CharField(max_length=255)

    def __str__(self):
        return self.nombreVacuna

class Medicamento(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.CharField(max_length=255)
    fechaUltimaCompra = models.DateField()
    cantidadExistente = models.IntegerField()
    cantidadMinima = models.IntegerField()

    def __str__(self):
        return self.nombre

class DuenioPerro(models.Model):
    apellido = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombres} {self.apellido}"

class EstadoEmpleado(models.Model):
    estudiante = models.CharField(max_length=255)
    recibido = models.CharField(max_length=255)
    trabaja = models.CharField(max_length=255)
    noTrabaja = models.CharField(max_length=255)

    def __str__(self):
        return self.estudiante

class RolEmpleado(models.Model):
    supervisor = models.CharField(max_length=255)
    supervisorSuplente = models.CharField(max_length=255)

    def __str__(self):
        return self.supervisor
