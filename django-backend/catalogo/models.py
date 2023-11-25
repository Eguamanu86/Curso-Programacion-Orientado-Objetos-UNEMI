from django.db import models

# Create your models here.
class ClienteCategoria (models.Model):
    codigo = models.CharField(max_length=20, verbose_name='Código')
    nombre = models.CharField(max_length=100, verbose_name='Descripción')

    def __str__(self):
        return self.nombre

    #Metadata
    class Meta :
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

class Cliente (models.Model):
    categoria = models.ForeignKey(ClienteCategoria, on_delete=models.CASCADE, blank=True, null=True)
    nombres = models.CharField(max_length=100,blank=True, null=True)
    nombre = models.CharField(max_length=50,blank=True, null=True)
    apellido = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return self.nombres

    #Metadata
    class Meta :
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['apellido']
