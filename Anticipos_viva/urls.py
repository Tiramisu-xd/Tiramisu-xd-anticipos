from django.urls import path
from django.conf import settings
 
from . import views

urlpatterns = [

    path('inicio_de_sesion',views.inicio_de_sesion,name='inicio_de_sesion'),

    path('item_cop',views.item_cop,name='item_cop'),
    
    path('item_pen',views.item_pen,name='item_pen'),
     
    path('item_usd',views.item_usd,name='item_usd'),

]