from django.db import models
from seguridad.constants import Gender
# Create your models here.
class ClienteCategoria (models.Model):
    codigo = models.CharField(max_length=20, verbose_name='Código')
    nombre = models.CharField(max_length=100, verbose_name='Descripción')
    orden = models.CharField(max_length=1024, blank=True, null=True, editable=False)
    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    activo = models.BooleanField(default=True, verbose_name="Estado")

    def __str__(self):
        return self.nombre

    class Meta :
        verbose_name = 'Cliente Categoria'
        verbose_name_plural = 'Cliente Categorias'
        ordering = ['nombre']

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.codigo:
            self.codigo = self.codigo.upper()

        if self.nombre:
            self.nombre = self.nombre.upper()

        try:
            user = get_current_user()

            if self._state.adding:
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self)

class Cliente (models.Model):
    categoria = models.ForeignKey(ClienteCategoria, on_delete=models.PROTECT, blank=True, null=True)
    codigo = models.CharField(max_length=15, blank=True, null=True, verbose_name='Código')
    identificador = models.CharField(max_length=10, verbose_name="C.Identidad", blank=True, null=True, unique=True)
    nombres = models.CharField(max_length=100,blank=True, null=True)
    nombre = models.CharField(max_length=50,blank=True, null=True)
    apellido = models.CharField(max_length=50,blank=True, null=True)
    genero = models.CharField(
        verbose_name="Genero",
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=10,
    )
    pais = models.ForeignKey('sistema.Pais', on_delete=models.PROTECT, blank=True, null=True)
    provincia = models.ForeignKey('sistema.Provincia', on_delete=models.PROTECT, blank=True, null=True)
    ciudad = models.ForeignKey('sistema.Ciudad', on_delete=models.PROTECT, blank=True, null=True)
    direccion = models.CharField(max_length=1024, verbose_name="Dirección", blank=True, null=True)
    telefono = models.CharField(max_length=20, verbose_name="Teléfono", blank=True, null=True)
    email = models.CharField(max_length=150, verbose_name="Email", blank=True, null=True)

    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    eliminadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    eliminadodate = models.DateTimeField(blank=True, null=True, editable=False)
    activo = models.BooleanField(default=True, verbose_name="Estado")

    def __str__(self):
        return self.nombres

    #Metadata
    class Meta :
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-editadodate']

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.codigo:
            self.codigo = self.codigo.upper()

        if self.nombre:
            self.nombre = self.nombre.upper()

        if self.apellido:
            self.apellido = self.apellido.upper()

        if self.direccion:
            self.direccion = self.direccion.upper()

        if self.email:
            self.email = self.email.lower()

        self.nombres = f'{self.nombre} {self.apellido}'.strip()

        try:
            user = get_current_user()

            if self._state.adding:
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self)
