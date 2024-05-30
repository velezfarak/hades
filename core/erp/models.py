from django.db import models
from datetime import datetime

CHOICES_SEXO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('X', 'No Binario'),
)

class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural = 'Los Tipos'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name='Categoría'
        verbose_name_plural = 'Las Categorias'
        ordering = ['id']

class Employee(models.Model):
    names = models.CharField(max_length=150, default='Sin Nombre', verbose_name='Apellidos y Nombres')
    dni = models.CharField(max_length=20, verbose_name='Identificación', unique=True)
    age = models.PositiveSmallIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    genero = models.CharField(max_length=1, choices=CHOICES_SEXO, null=True, blank=True)
    type = models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    avatar = models.ImageField(upload_to='avatar/%y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%y/%m/%d', null=True, blank=True)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
    date_creation = models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')
    date_update = models.DateField(auto_now_add=True, verbose_name='Fecha de Modificación')
    state = models.BooleanField(default=True)

    def __str(self):
        return self.names

    class Meta:
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Los Empleados'
        ordering = ['id']

