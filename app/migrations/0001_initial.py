# Generated by Django 4.2.4 on 2023-11-10 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudia', models.BooleanField(default=False)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroDocumento', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EstadoEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialMascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadoPerro', models.CharField(max_length=255)),
                ('rolPersona', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialRol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('laboratorio', models.CharField(max_length=255)),
                ('fechaUltimaCompra', models.DateField()),
                ('cantidadExistente', models.IntegerField()),
                ('cantidadMinima', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePersona', models.CharField(max_length=255)),
                ('numDocPersona', models.IntegerField()),
                ('descripcion', models.CharField(max_length=180, verbose_name='Descripcion:')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=255)),
                ('pesoMinimoMachos', models.FloatField()),
                ('pesoMaximoMachos', models.FloatField()),
                ('pesoMinimoHembras', models.FloatField()),
                ('pesoMaximoHembras', models.FloatField()),
                ('alturaMediaMachos', models.FloatField()),
                ('alturaMediaHembras', models.FloatField()),
                ('cuidadosEspeciales', models.CharField(max_length=180, verbose_name='cuidadosEspeciales')),
            ],
        ),
        migrations.CreateModel(
            name='Requerimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreVacuna', models.CharField(max_length=255)),
                ('empleado', models.CharField(max_length=255)),
                ('laboratorio', models.CharField(max_length=255)),
                ('dosis', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vacunacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaProgramada', models.DateField()),
                ('fechaReal', models.DateField()),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('fechaNacimiento', models.DateField()),
                ('pesoActual', models.FloatField()),
                ('alturaActual', models.FloatField()),
                ('consulta', models.TextField()),
                ('vacuna', models.CharField(max_length=100, verbose_name='vacuna;')),
                ('historialMascotas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.historialmascotas')),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.raza')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaEntrada', models.DateField()),
                ('sIntomas', models.CharField(max_length=255)),
                ('diagnosticos', models.CharField(max_length=255)),
                ('medicamento', models.CharField(max_length=255)),
                ('fechaSalida', models.DateField()),
                ('perro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='app.perro')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('nombres', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('fechaNacimiento', models.DateField(null=True)),
                ('fechaIngreso', models.DateField(null=True)),
                ('empleado', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('sucursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.sucursal')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
