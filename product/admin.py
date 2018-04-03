from django.contrib import admin

# Register your models here.
from .models import Shop, Product, Category

admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Category)