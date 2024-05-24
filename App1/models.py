from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator, EmailValidator



class UsuarioDb(models.Model):
    dni = models.CharField(
        max_length=8,
        default='',
        validators=[MinLengthValidator(8), RegexValidator(r'^\d{8}$', message='El DNI debe contener exactamente 8 dígitos.')]
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100) 
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator(message="Por favor, introduce una dirección de correo electrónico válida")]
        )
    password = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class CanchaDb(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    
    def __str__(self) -> str:
        return self.nombre

class ReservaDb(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    usuario = models.ForeignKey(UsuarioDb, on_delete=models.CASCADE)
    cancha = models.ForeignKey(CanchaDb, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('fecha', 'hora', 'cancha')
    
    def estado(self):
        if ReservaDb.objects.filter(fecha=self.fecha, hora=self.hora, cancha=self.cancha).exists():
            raise ValidationError('La cancha ya está reservada para esta fecha y hora.')
    
    def save(self, *args, **kwargs):
        self.estado()
        super().save(*args, **kwargs)
        

    def __str__(self) -> str:
        return f"Cancha {self.cancha} reservada para el dia {self.fecha} {self.hora} horas  "
    


