from django.urls import path, re_path
from . import views

# URLConf
urlpatterns = [
    #path('hello/', views.text)
    re_path(r'product/(?P<product_id>\w+)/$', views.product, name = 'product')
]