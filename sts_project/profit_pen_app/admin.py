from django.contrib import admin

# Register your models here.
from .models import RawMaterial,Product,RawMaterialQuantities,ProductQuantities,ProductPrices,RawMaterialPrices

admin.site.register(RawMaterial)
admin.site.register(Product)
admin.site.register(RawMaterialQuantities)
admin.site.register(ProductQuantities)
admin.site.register(ProductPrices)
admin.site.register(RawMaterialPrices)