from django.db import models


class Sucursal(models.Model):
    direccion = models.CharField(max_length=255)

    def agregarEmpleado(self, empleado):
        self.empleados.append(empleado)

    def agregarConsulta(self, consulta):
        self.consultas.append(consulta)

class Empleado(models.Model):
    numeroDocumento = models.IntegerField()
    nombres = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fechaNacimiento = models.DateField()
    fechaIngreso = models.DateField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)


class AsignacionEmpleados(models.Model):
    fechaIngreso = models.DateField()
    fechaEgreso = models.DateField()
    descripcion = models.CharField(max_length=255)



    def verificarEstadoEmpleado(self):
        # Implementar lógica para verificar el estado del empleado
        pass

    def verificarRolEmpleado(self):
        # Implementar lógica para verificar el rol del empleado
        pass

 
class Perro(models.Model):
    numeroHistoriaClinica = models.IntegerField()
    nombre = models.CharField(max_length=255)
    fechaNacimiento = models.DateField()
    raza = models.ForeignKey('Raza', on_delete=models.CASCADE)
    pesoActual = models.FloatField()
    alturaActual = models.FloatField()
    historialMascotas = models.ForeignKey('HistorialMascotas', on_delete=models.CASCADE)
    consulta = models.TextField()  
    vacuna = models.CharField(("vacuna;"), max_length=100)

    def generarNumHistoriaClinica(self):
        # Implementar lógica para generar el número de historia clínica
        pass

    def verificarPersona(self):
        # Implementar lógica para verificar la persona asociada al perro
        pass

    def identificarVacunacion(self):
        # Implementar lógica para identificar la vacunación del perro
        pass

class HistorialMascotas(models.Model):
    estadoPerro = models.CharField(max_length=255)
    rolPersona = models.CharField(max_length=255)

    def verificarEstadoPerro(self):
        # Implementar lógica para verificar el estado del perro
        pass

    def verificarRolPersona(self):
        # Implementar lógica para verificar el rol de la persona
        pass

class Persona(models.Model):
    nombrePersona = models.CharField(max_length=255)
    numDocPersona = models.IntegerField()
    descripcion = models.CharField(("Descripcion:"), max_length=180)


class Raza(models.Model):
    denominacion = models.CharField(max_length=255)
    pesoMinimoMachos = models.FloatField()
    pesoMaximoMachos = models.FloatField()
    pesoMinimoHembras = models.FloatField()
    pesoMaximoHembras = models.FloatField()
    alturaMediaMachos = models.FloatField()
    alturaMediaHembras = models.FloatField()
    cuidadosEspeciales = models.CharField(("cuidadosEspeciales"), max_length=180)

  
class Consulta(models.Model):
    numeroOrden = models.IntegerField()
    fechaEntrada = models.DateField()
    sIntomas = models.CharField(max_length=255)
    diagnosticos = models.CharField(max_length=255)
    medicamento = models.CharField(max_length=255)
    fechaSalida = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE, related_name='consultas')

    def verificarPersona(self):
        # Implementar lógica para verificar la persona asociada a la consulta
        pass

    def verificarRolEmpleadoConsulta(self):
        # Implementar lógica para verificar el rol del empleado en la consulta
        pass

    def identificarNumHistoriaClinica(self):
        # Implementar lógica para identificar el número de historia clínica asociado
        pass

    def recetarMedicamentos(self):
        # Implementar lógica para recetar medicamentos
        pass

    def verificarPerro(self):
        # Implementar lógica para verificar el perro asociado a la consulta
        pass

class Vacunacion(models.Model):
    fechaProgramada = models.DateField()
    fechaReal = models.DateField()
    descripcion = models.CharField(max_length=255)

class Vacuna(models.Model):
    nombreVacuna = models.CharField(max_length=255)
    empleado = models.CharField(max_length=255)
    laboratorio = models.CharField(max_length=255)
    dosis = models.CharField(max_length=255)

class Medicamento(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.CharField(max_length=255)
    fechaUltimaCompra = models.DateField()
    cantidadExistente = models.IntegerField()
    cantidadMinima = models.IntegerField()

class EstadoEmpleado(models.Model):
    estudiante = models.CharField(max_length=255)
    recibido = models.CharField(max_length=255)
    trabaja = models.CharField(max_length=255)
    noTrabaja = models.CharField(max_length=255)

class RolEmpleado(models.Model):
    supervisor = models.CharField(max_length=255)
    supervisorSuplente = models.CharField(max_length=255)
