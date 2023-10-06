from django.db import models

class Sucursal(models.Model):
    direccion = models.CharField(max_length=255)
    
    def __init__(self, direccion):
        self.direccion = direccion
        self.empleados = []
        self.consultas = []

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

    def __init__(self, numeroDocumento, nombres, apellido, fechaNacimiento, fechaIngreso):
        self.numeroDocumento = numeroDocumento
        self.nombres = nombres
        self.apellido = apellido
        self.fechaNacimiento = fechaNacimiento
        self.fechaIngreso = fechaIngreso
        self.sucursal = None

class AsignacionEmpleados(models.Model):
    fechaIngreso = models.DateField()
    fechaEgreso = models.DateField()
    descripcion = models.TextField()

    def __init__(self, fechaIngreso, fechaEgreso, descripcion):
        self.fechaIngreso = fechaIngreso
        self.fechaEgreso = fechaEgreso
        self.descripcion = descripcion

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
    vacuna = models.TextField()

    def __init__(self, nombre, fechaNacimiento, raza, pesoActual, alturaActual):
        self.numeroHistoriaClinica = None
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.raza = raza
        self.pesoActual = pesoActual
        self.alturaActual = alturaActual
        self.historialMascotas = []

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

    def __init__(self, estadoPerro, rolPersona):
        self.estadoPerro = estadoPerro
        self.rolPersona = rolPersona

    def verificarEstadoPerro(self):
        # Implementar lógica para verificar el estado del perro
        pass

    def verificarRolPersona(self):
        # Implementar lógica para verificar el rol de la persona
        pass

class Persona(models.Model):
    nombrePersona = models.CharField(max_length=255)
    numDocPersona = models.IntegerField()
    descripcion = models.TextField()

    def __init__(self, nombrePersona, numDocPersona, descripcion):
        self.nombrePersona = nombrePersona
        self.numDocPersona = numDocPersona
        self.descripcion = descripcion


class Raza(models.Model):
    denominacion = models.CharField(max_length=255)
    pesoMinimoMachos = models.FloatField()
    pesoMaximoMachos = models.FloatField()
    pesoMinimoHembras = models.FloatField()
    pesoMaximoHembras = models.FloatField()
    alturaMediaMachos = models.FloatField()
    alturaMediaHembras = models.FloatField()
    cuidadosEspeciales = models.TextField()

    def __init__(self, denominacion, pesoMinimoMachos, pesoMaximoMachos, pesoMinimoHembras,
                 pesoMaximoHembras, alturaMediaMachos, alturaMediaHembras, cuidadosEspeciales):
        self.denominacion = denominacion
        self.pesoMinimoMachos = pesoMinimoMachos
        self.pesoMaximoMachos = pesoMaximoMachos
        self.pesoMinimoHembras = pesoMinimoHembras
        self.pesoMaximoHembras = pesoMaximoHembras
        self.alturaMediaMachos = alturaMediaMachos
        self.alturaMediaHembras = alturaMediaHembras
        self.cuidadosEspeciales = cuidadosEspeciales


class Consulta(models.Model):
    numeroOrden = models.IntegerField()
    fechaEntrada = models.DateField()
    sIntomas = models.TextField()
    diagnosticos = models.TextField()
    medicamento = models.TextField()
    fechaSalida = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)

    def __init__(self, numeroOrden, fechaEntrada, sintomas, diagnosticos, medicamento, fechaSalida):
        self.numeroOrden = numeroOrden
        self.fechaEntrada = fechaEntrada
        self.sintomas = sintomas
        self.diagnosticos = diagnosticos
        self.medicamento = medicamento
        self.fechaSalida = fechaSalida
        self.listaEmpleados = []

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
    descripcion = models.TextField()

    def __init__(self, fechaProgramada, fechaReal, descripcion):
        self.fechaProgramada = fechaProgramada
        self.fechaReal = fechaReal
        self.descripcion = descripcion

class Vacuna(models.Model):
    nombreVacuna = models.CharField(max_length=255)
    empleado = models.CharField(max_length=255)
    laboratorio = models.CharField(max_length=255)
    dosis = models.CharField(max_length=255)

    def __init__(self, nombreVacuna, empleado, laboratorio, dosis):
        self.nombreVacuna = nombreVacuna
        self.empleado = empleado
        self.laboratorio = laboratorio
        self.dosis = dosis

class Medicamento(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.CharField(max_length=255)
    fechaUltimaCompra = models.DateField()
    cantidadExistente = models.IntegerField()
    cantidadMinima = models.IntegerField()

    def __init__(self, nombre, laboratorio, fechaUltimaCompra, cantidadExistente, cantidadMinima):
        self.nombre = nombre
        self.laboratorio = laboratorio
        self.fechaUltimaCompra = fechaUltimaCompra
        self.cantidadExistente = cantidadExistente
        self.cantidadMinima = cantidadMinima

class EstadoEmpleado(models.Model):
    estudiante = models.CharField(max_length=255)
    recibido = models.CharField(max_length=255)
    trabaja = models.CharField(max_length=255)
    noTrabaja = models.CharField(max_length=255)

    def __init__(self, estudiante, recibido, trabaja, noTrabaja):
        self.estudiante = estudiante
        self.recibido = recibido
        self.trabaja = trabaja
        self.noTrabaja = noTrabaja

class RolEmpleado(models.Model):
    supervisor = models.CharField(max_length=255)
    supervisorSuplente = models.CharField(max_length=255)

    def __init__(self, supervisor, supervisorSuplente):
        self.supervisor = supervisor
        self.supervisorSuplente = supervisorSuplente

