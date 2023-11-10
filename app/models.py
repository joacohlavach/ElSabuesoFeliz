from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("El campo de nombre de usuario es obligatorio")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")

class Sucursal(models.Model):
    direccion = models.CharField(max_length=255)

    def agregarEmpleado(self, empleado):
        self.empleados.append(empleado)

    def agregarConsulta(self, consulta):
        self.consultas.append(consulta)
        
    def __str__(self) -> str:
        return self.direccion()

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    nombres = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fechaNacimiento = models.DateField(null=True null=True)
    fechaIngreso = models.DateField(null=True null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True)
    empleado = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(unique=True, null=True)


    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "nombres", "apellido"]


    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} - {self.nombres} {self.apellido}"

class DetalleEmpleado(models.Model):
    estudia = models.BooleanField(default=False)
    cantidad = models.IntegerField(null=True, blank=True)

    def verificarEstadoEmpleado(self):
        # Implementar logica para verificar estado empleado
        pass

class Requerimiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre()
    
class HistorialEmpleado(models.Model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    descripcion = models.CharField(max_length=255)

class EstadoEmpleado(models.Model):
    estado = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.estado()
    
class HistorialRol(models.Model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    descripcion = models.CharField(max_length=255)

class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre()
class Perro(models.Model):
    nombre = models.CharField(max_length=255)
    fechaNacimiento = models.DateField()
    raza = models.ForeignKey('Raza', on_delete=models.CASCADE)
    pesoActual = models.FloatField()
    alturaActual = models.FloatField()
    historialMascotas = models.ForeignKey('HistorialMascotas', on_delete=models.CASCADE)
    consulta = models.TextField()  
    vacuna = models.CharField(("vacuna;"), max_length=100)

    def __str__(self) -> str:
        return self.nombre()

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

    def __str__(self) -> str:
        return self.nombrePersona()

class Raza(models.Model):
    denominacion = models.CharField(max_length=255)
    pesoMinimoMachos = models.FloatField()
    pesoMaximoMachos = models.FloatField()
    pesoMinimoHembras = models.FloatField()
    pesoMaximoHembras = models.FloatField()
    alturaMediaMachos = models.FloatField()
    alturaMediaHembras = models.FloatField()
    cuidadosEspeciales = models.CharField(("cuidadosEspeciales"), max_length=180)

    def __str__(self) -> str:
        return self.denominacion()

class Consulta(models.Model):
    fechaEntrada = models.DateField()
    sIntomas = models.CharField(max_length=255)
    diagnosticos = models.CharField(max_length=255)
    medicamento = models.CharField(max_length=255)
    fechaSalida = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE, related_name='consultas')

    def __str__(self) -> str:
        return self.Consulta()

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

    def __str__(self) -> str:
        return self.descripcion()

class Vacuna(models.Model):
    nombreVacuna = models.CharField(max_length=255)
    empleado = models.CharField(max_length=255)
    laboratorio = models.CharField(max_length=255)
    dosis = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombreVacuna()

class Medicamento(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.CharField(max_length=255)
    fechaUltimaCompra = models.DateField()
    cantidadExistente = models.IntegerField()
    cantidadMinima = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre()

