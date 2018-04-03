from django.conf import settings
from django.db import models


from product.models import Product

class UserProducts(models.Model):
    # settings.AUTH_USER_MODEL identify current login user
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    substitution = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='substitution')
