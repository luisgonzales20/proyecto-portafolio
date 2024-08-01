from django.db import models

# Create your models here.
#Modelo para formacion
class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    degree_title = models.CharField(max_length=300, verbose_name='Titulo Obtenido')
    description = models.TextField(verbose_name='Descripcion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificacion')

    class Meta:
        verbose_name = 'formacion'
        verbose_name_plural = 'formaciones'
        ordering = ['-created']

    def __str__(self):
        return self.title

# Modelo para Skill
class Skill(models.Model):
    title = models.CharField(max_length=80, verbose_name='Titulo')
    image = models.ImageField(upload_to='skills', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificacion')

    class Meta:
        verbose_name = 'conocimiento'
        verbose_name_plural = 'conocimientos'
        ordering = ['-created']

    def __str__(self):
        return self.title
