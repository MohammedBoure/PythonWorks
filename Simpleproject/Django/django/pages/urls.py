from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('admin/',views.admin,name='admin'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('product_management/',views.product_management,name='product_management'),
    path('upload_product/', views.upload_product, name='upload_product'),
]