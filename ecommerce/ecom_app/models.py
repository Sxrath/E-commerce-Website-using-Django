from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=500)
    category = models.CharField(max_length=200)
    available = models.BooleanField(default=True)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, through='CartItems', related_name='carts')
    total_price=models.DecimalField(max_digits=10,decimal_places=5,default=Decimal('0.00'))
class CartItems(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity