from django.contrib import admin

# Register your models here.
from .models import RawMaterial,Product,RawMaterialQuantities

admin.site.register(RawMaterial)
admin.site.register(Product)
admin.site.register(RawMaterialQuantities)