from django.db import models

# Create your models here.
class ProductoCategoria (models.Model):
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
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-editadodate']

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.codigo:
            self.codigo = self.codigo.upper()

        if self.nombre:
            self.nombre = self.nombre.upper()

        try:
            user = get_current_user()

            if self._state.adding: ## si estamos creando registro
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self) ## se persiste el dato

class Proveedor (models.Model):
    codigo = models.CharField(max_length=15, blank=True, null=True, verbose_name='Código')
    identificador = models.CharField(max_length=10, verbose_name="Ruc", blank=True, null=True, unique=True)
    nombres = models.CharField(max_length=100,blank=True, null=True)
    representante = models.CharField(max_length=100,blank=True, null=True)
    pais = models.ForeignKey('sistema.Pais', on_delete=models.PROTECT, blank=True, null=True)
    provincia = models.ForeignKey('sistema.Provincia', on_delete=models.PROTECT, blank=True, null=True)
    ciudad = models.ForeignKey('sistema.Ciudad', on_delete=models.PROTECT, blank=True, null=True)
    direccion = models.CharField(max_length=1024, verbose_name="Dirección", blank=True, null=True)
    telefono = models.CharField(max_length=20, verbose_name="Teléfono", blank=True, null=True)
    email = models.CharField(max_length=150, verbose_name="Email", blank=True, null=True)
    web = models.CharField(max_length=150, blank=True, null=True)

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
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['-editadodate']

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.codigo:
            self.codigo = self.codigo.upper()

        if self.nombres:
            self.nombres = self.nombres.upper()

        if self.direccion:
            self.direccion = self.direccion.upper()

        if self.email:
            self.email = self.email.lower()

        if self.web:
            self.web = self.web.lower()


        try:
            user = get_current_user()

            if self._state.adding:
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self)

class Marca (models.Model):
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
        verbose_name = 'Marca'
        verbose_name_plural = 'Marca'
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

class Producto (models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, blank=True, null=True)
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.PROTECT, blank=True, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, blank=True, null=True)

    codigo = models.CharField(max_length=15, blank=True, null=True, verbose_name='Código')
    nombre = models.CharField(max_length=80,blank=True, null=True)
    descripcion = models.CharField(max_length=200,verbose_name='Descripción',blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True,default='')
    ubicacion = models.CharField(max_length=50, blank=True, null=True,default='')
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,default=0)
    modelo = models.CharField(max_length=50, blank=True, null=True,default='')
    procedencia = models.CharField(max_length=50, blank=True, null=True,default='')
    stock_maximo = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True,default=0)
    stock_minimo = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True,default=0)
    empaque = models.CharField(max_length=10, blank=True, null=True,default='')
    costo_compra = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True,default=0)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True,default=0)

    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    eliminadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    eliminadodate = models.DateTimeField(blank=True, null=True, editable=False)

    activo = models.BooleanField(default=True, verbose_name="Estado")

    def __str__(self):
        return self.nombre

    class Meta :
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-editadodate']

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.codigo:
            self.codigo = self.codigo.upper()

        if self.nombre:
            self.nombre = self.nombre.upper()

        if self.descripcion:
            self.descripcion = self.descripcion.upper()

        try:
            user = get_current_user()

            if self._state.adding:
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self)
