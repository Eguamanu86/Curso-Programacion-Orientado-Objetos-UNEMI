from crum import get_current_user
from django.db import models

class Pais(models.Model):
    codigo = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True,verbose_name='Pais')
    nombre_corto = models.CharField(max_length=50,verbose_name='Abrev.',blank=True, null=True)
    orden = models.CharField(max_length=1024, blank=True, null=True, editable=False)
    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ['nombre']

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.codigo:
            self.codigo = self.codigo.upper()

        if self.nombre:
            self.nombre = self.nombre.upper()

        if self.nombre_corto:
            self.nombre_corto = self.nombre_corto.upper()

        try:
            user = get_current_user()

            if self._state.adding:
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self)

class Provincia(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True,verbose_name='Provincia')
    nombre_corto = models.CharField(max_length=50,verbose_name='Abrev.',blank=True, null=True)
    orden = models.CharField(max_length=1024, blank=True, null=True, editable=False)
    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        ordering = ['nombre']

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.codigo:
            self.codigo = self.codigo.upper()

        if self.nombre:
            self.nombre = self.nombre.upper()

        if self.nombre_corto:
            self.nombre_corto = self.nombre_corto.upper()

        try:
            user = get_current_user()

            if self._state.adding:
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self)

class Ciudad(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True,verbose_name='Ciudad')
    nombre_corto = models.CharField(max_length=50,verbose_name='Abrev.',blank=True, null=True)
    orden = models.CharField(max_length=1024, blank=True, null=True, editable=False)
    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['nombre']

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.codigo:
            self.codigo = self.codigo.upper()

        if self.nombre:
            self.nombre = self.nombre.upper()

        if self.nombre_corto:
            self.nombre_corto = self.nombre_corto.upper()

        try:
            user = get_current_user()

            if self._state.adding:
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self)
