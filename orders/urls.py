from django.urls import path, re_path
from . import views

# URLConf
urlpatterns = [
    re_path(r'^basket_adding/$', views.basket_adding, name = 'basket_adding'),
    re_path(r'^checkout/$', views.checkout, name = 'checkout'),
]