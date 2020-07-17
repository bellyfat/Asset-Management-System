from django.urls import path
from . import views

urlpatterns = [
    path('log', views.log, name='log'),
    path('log/home', views.home, name='home'),
    path('log/assets', views.assets, name='assets'),
    path('log/purchases', views.purchases, name='purchases'),
    path('log/adduser', views.adduser, name='adduser'),
    path('log/addasset', views.addasset, name='addasset'),   
    path('log/addpurchase', views.addpurchase, name='addpurchase')     
]