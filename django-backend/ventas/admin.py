from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Vendedor)
admin.site.register(Venta)
admin.site.register(VentaDetalle)
