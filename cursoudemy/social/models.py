from django.db import models

# Create your models here.

class link(models.Model):
    key = models.SlugField(verbose_name="Nombre Clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red socuial", max_length=200) 
    url = models.URLField(verbose_name="Rnlace", max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de modificacion")

class Meta:
    verbose_name = "enlace"
    verbose_name_plural = "enlaces"
    ordering = ['name']

def __str__(self):
    return self.name