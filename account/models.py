from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class UserProducts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    substitution = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='substitution')
