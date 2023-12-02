from django.db import models
from seguridad.constants import Gender

class Vendedor (models.Model):
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
    ciudad = models.ForeignKey('sistema.Ciudad', on_delete=models.CASCADE, blank=True, null=True)
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
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
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

# Create your models here.
class Venta(models.Model):

    TIPO_DOCUMENTO_FACTURA = (
        ('VEN-FA','VEN-FA'),
        ('POS-NV','POS-NV'),
        ('POS-FA','POS-FA'),
    )

    numero = models.CharField(max_length=10,verbose_name='Número', blank=True,null=True)
    cliente = models.ForeignKey('catalogo.Cliente', on_delete=models.PROTECT, blank=True, null=True)
    detalle = models.CharField(max_length=100, blank=True, null=True,default='', editable=False)
    identificador = models.CharField(max_length=13, blank=True, null=True,default='', editable=False)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.PROTECT, blank=True, null=True)
    secuencia = models.CharField(max_length=20, blank=True, null=True,default='')
    contado = models.BooleanField(default=False)
    fecha = models.DateTimeField(blank=True,null=True)
    tipo = models.CharField(max_length=10,choices=TIPO_DOCUMENTO_FACTURA)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True,default=0)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True,default=0)
    impuesto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True,default=0)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True,default=0)
    efectivo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True,default=0)
    nota = models.CharField(max_length=200, blank=True, null=True,default='')
    forma_pago = models.CharField(max_length=3, blank=True, null=True)
    vuelto_cliente = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True,default=0)
    anulado = models.BooleanField(default=False)

    creadopor = models.CharField(max_length=15, blank=True, null=True,editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,blank=True, null=True,editable=False)
    editadopor = models.CharField(max_length=15, blank=True, null=True,editable=False)
    editadodate = models.DateTimeField(auto_now=True, blank=True, null=True,editable=False)
    anuladonota = models.CharField(max_length=1024, blank=True, null=True,editable=False)
    anuladopor = models.CharField(max_length=15, blank=True, null=True,editable=False)
    anuladodate = models.DateTimeField(blank=True, null=True,editable=False)

    def __str__(self):
        return self.detalle

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['-fecha']

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.detalle = self.cliente.nombres
        self.identificador = self.cliente.identificador
        try:
            user = get_current_user()
            if self._state.adding:
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self)

class VentaDetalle(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE,blank=True, null=True)
    producto = models.ForeignKey('inventario.Producto', on_delete=models.PROTECT, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=11, decimal_places=2,default=0)
    costo = models.DecimalField(max_digits=19, decimal_places=4,default=0)
    precio = models.DecimalField(max_digits=19, decimal_places=4,default=0)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4,default=0)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True,default=0)
    impuesto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True,default=0)
    total = models.DecimalField(max_digits=19, decimal_places=4,default=0)
    empaque = models.CharField(max_length=40, blank=True, null=True,default='')

    creadopor = models.CharField(max_length=15, blank=True, null=True,editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,blank=True, null=True,editable=False)
    editadopor = models.CharField(max_length=15, blank=True, null=True,editable=False)
    editadodate = models.DateTimeField(auto_now=True,blank=True, null=True,editable=False)

    def __str__(self):
        return self.producto.nombre

    class Meta:
        verbose_name = 'Venta Detalle'
        verbose_name_plural = 'Venta Detalles'

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        try:
            user = get_current_user()
            if self._state.adding:
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self)
