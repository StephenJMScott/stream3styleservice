from django.conf.urls import url
from django.contrib import admin
from products.views import get_products, do_search, product_details

urlpatterns=[
    url(r'^$', get_products, name="productlist"),
    url(r'^search/', do_search, name="search"),
    url(r'^(\d+)$', product_details, name='product_details'),
    ]