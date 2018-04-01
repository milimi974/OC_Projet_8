from django.contrib import admin

# Register your models here.
from .models import Shop, Products, Category

admin.site.register(Products)
admin.site.register(Shop)
admin.site.register(Category)