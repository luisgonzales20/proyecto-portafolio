from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(upload_to='projects', verbose_name='Imagen')
    link = models.URLField(max_length=180, blank=True, null=True, verbose_name='Enlace')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificacion')

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
        ordering = ['-created']

    #Para que me miestre el nombre del proyecto que estoy agregando
    def __str__(self):
        return self.title