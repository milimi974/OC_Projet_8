from django.conf import settings
from django.db import models


from product.models import Product

class UserProduct(models.Model):
    # settings.AUTH_USER_MODEL identify current login user

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product', blank=False, null=True)
    substitution = models.ManyToManyField(Product, related_name='substitution')