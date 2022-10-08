from enum import unique
from django.db import models

# Create your models here.


class Person(models.Model):
    document_types = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('TI', 'Tarjeta de Identidad'),
        ('RC', 'Registro Civil'),
        ('PA', 'Pasaporte'),
        ('MS', 'Menor Sin Identificación'),
        ('AS', 'Adulto Sin Identificación'),
        ('NI', 'NIT'),
        ('NU', 'Número Único de Identificación'),
        ('OT', 'Otro'),
    ]

    document_type = models.CharField(
        max_length=2, choices=document_types, blank=False, null=False)
    document_number = models.IntegerField(unique=True, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    hobbies = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
