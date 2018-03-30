# Mocks contain data for test
from django.http import Http404

class Products:

    PRODUCTS = [
        {'id' : 1, 'name' : 'Viande de boeuf', 'nutri_code' : 'a', 'picture' : 'img/portfolio/thumbnails/1.jpg'},
        {'id' : 2, 'name' : 'raisin blanc', 'nutri_code' : 'b', 'picture' : 'img/portfolio/thumbnails/2.jpg'},
        {'id' : 3, 'name' : 'céréale', 'nutri_code' : 'a', 'picture' : 'img/portfolio/thumbnails/3.jpg'},
        {'id' : 4, 'name' : 'Viande de poisson', 'nutri_code' : 'c', 'picture' : 'img/portfolio/thumbnails/4.jpg'},
        {'id' : 5, 'name' : 'Farine', 'nutri_code' : 'd', 'picture' : 'img/portfolio/thumbnails/5.jpg'},
        {'id' : 6, 'name' : 'Viande de poulet', 'nutri_code' : 'a', 'picture' : 'img/portfolio/thumbnails/6.jpg'},
    ]

    @classmethod
    def all(cls):
        return cls.PRODUCTS

    @classmethod
    def find(cls, id):
        try:
            return cls.PRODUCTS[int(id) - 1]
        except:
            return Http404('')