from django.contrib import admin

# Register your models here.
from .models import RawMaterial,Product,RawMaterialQuantities,ProductQuantities,ProductPrices,RawMaterialPrices,ProductSales,RawMaterialSales


admin.site.register(RawMaterial)
admin.site.register(Product)
admin.site.register(RawMaterialQuantities)
admin.site.register(ProductQuantities)
admin.site.register(ProductPrices)
admin.site.register(RawMaterialPrices)
admin.site.register(ProductSales)
admin.site.register(RawMaterialSales)