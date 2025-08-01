from django.db import models

# Create your models here.
class Instructor(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cedula de Ciudadanía'),
        ('CE', 'Cedula de extranjeria'),
        ('TI', 'Tarja de Identidad'),
        ('PAS', 'Pasaporte'),
    ]
    
    NIVEL_EDUCATIVO_CHOICES = [
        ('TEC', 'Tecnico'),
        ('TGL', 'Tecnologo'),
        ('PRE', 'Pregrado'),
        ('ESP', 'Especializacion'),
        ('MAE', 'Maestria'),
        ('DOC', 'Doctorado'),
    ]
    
    documento_identidad = models.CharField(max_length=20, unique=True)
    tipo_documento = models.CharField(max_length=3, choices=TIPO_DOCUMENTO_CHOICES, default='CC')
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200, null=True)
    correo = models.EmailField(null=True)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=200, null=True)
    nivel_educativo = models.CharField(max_length=3, choices=NIVEL_EDUCATIVO_CHOICES, default='MAE')
    especialidad = models.CharField(max_length=200)
    anos_experiencia = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    fecha_vinculacion = models.DateField(null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.especialidad}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
