from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    """ Categories of product
        :argument
        model : parent

    """
    # fields
    name = models.CharField(max_length=255, unique=True)


class Shop(models.Model):
    """ Shops of product
        :argument
        model : parent

    """
    # fields
    name = models.CharField(max_length=255, unique=True)


class Products(models.Model):
    """ Product class
        :argument
        model : parent

    """
    # fields
    name = models.CharField(max_length=255)
    description = models.TextField()
    nutri_code = models.CharField(max_length=1)
    link = models.CharField(max_length=255)
    picture = models.URLField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='products', blank=True)
    shops = models.ManyToManyField(Shop, related_name='products', blank=True)
    users = models.ManyToManyField(User, related_name='products', blank=True)

