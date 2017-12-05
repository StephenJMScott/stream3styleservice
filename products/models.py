# Create your models here.
from __future__ import unicode_literals
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name
        
        
class Categories(models.Model):
    name=models.CharField(max_length=50)
    parent= models.ForeignKey('self', null=True, blank=True)
    products= models.ManyToManyField(Product, blank=True)
    
    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images')
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return str(self.image)
    