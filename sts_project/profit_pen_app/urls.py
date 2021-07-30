from django.urls import path
from django.conf.urls import url

from profit_pen_app import views

urlpatterns = [
    path('', views.index, name='index'),

    path('supply',views.create_supply , name='get_supply'),
    path('view_supply',views.view_supply , name = 'view_supplies')
     
]
