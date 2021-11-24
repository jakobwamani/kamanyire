from django.urls import path
from django.conf.urls import url

from profit_pen_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('supply',views.create_supply , name='get_supply'),
    path('view_supply',views.viewing_supply , name = 'view_supplies'),
    path('update_supply/',views.updating_supply , name = 'update_supplies'),
    path('delete_supply/',views.delete_supply , name = 'delete_supplies'),
    path('product/',views.create_product , name = 'create_products'),
    path('view_product/',views.viewing_product , name = 'view_products'),
    path('update_product/',views.updating_product , name = 'update_products'),
    path('delete_product/',views.deleting_product , name = 'delete_products'),
    path('create_product_price/',views.create_product_price , name = "create_product_prices"),
    path('view_product_prices/',views.viewing_product_prices , name = "view_product_prices"),
    path('update_product_prices/',views.updating_product_prices , name = "update_product_prices"),
    path('delete_product_prices/',views.deleting_product_prices , name = "delete_product_prices"),
    path('create_raw_material_prices/',views.create_raw_material_prices, name = "create_raw_material_prices"),
    path('view_raw_material_prices/',views.view_raw_material_prices, name = "view_raw_material_prices"), 
    path('update_raw_material_prices/',views.update_raw_material_prices, name = "update_raw_material_prices"),
    path('delete_raw_material_prices/',views.deleting_raw_material_prices, name = "delete_raw_material_prices"),
    path('view_product_catalog',views.viewing_product_catalog, name = "view_product_catalog"),
    path('view_raw_material_catalog',views.viewing_raw_material_catalog, name = "view_raw_material_catalog"),
]
