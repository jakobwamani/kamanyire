from django.urls import path
from django.conf.urls import url

from profit_pen_app import views

urlpatterns = [
    path('', views.index, name='index'),

    path('supply',views.create_supply , name='get_supply'),
    path('view_supply',views.viewing_supply , name = 'view_supplies'),
    path('update_supply/',views.updating_supply , name = 'update_supplies')
     
]
