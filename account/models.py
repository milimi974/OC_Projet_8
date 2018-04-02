from django.db import models
from django.contrib.auth.models import User
from product.models import Products

class UserProducts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product')
    substitution = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='substitution')
