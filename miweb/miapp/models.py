from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    asignatura = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    asignatura = models.CharField(max_length=100)

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100)
    camada = models.CharField(max_length=100)

