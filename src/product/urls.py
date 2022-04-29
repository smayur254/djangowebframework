from django.contrib import admin
from django.urls import path

from product.views import  createform, product, dynamic_lookup_view, product_delete, updateform


urlpatterns = [
    path('form/',createform, name='form'),
    path('<int:id>/update',updateform, name='updateform'),
    path('',product, name='product'),
    # path('product/<int:my_id>/',productDetail, name='form'),
    path('<int:id>/',dynamic_lookup_view, name='productDetail'),
    # path('product/delete/<int:id>',product_delete, name='productdelete'),
    path('<int:id>/delete',product_delete, name='productdelete'),
]
