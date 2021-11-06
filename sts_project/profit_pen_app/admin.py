from django.contrib import admin

# Register your models here.
from .models import RawMaterial,Product,RawMaterialQuantities,ProductQuantities

admin.site.register(RawMaterial)
admin.site.register(Product)
admin.site.register(RawMaterialQuantities)
admin.site.register(ProductQuantities)