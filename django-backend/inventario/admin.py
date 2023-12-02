from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.register(ProductoCategoria)
admin.site.register(Proveedor)
admin.site.register(Marca)
admin.site.register(Producto)
