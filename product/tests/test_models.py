import pytest
from mixer.backend.django import mixer
from types import *
from product.models import Category

pytestmark = pytest.mark.django_db

class TestProduct:

    def test_model(self):
        obj = mixer.blend('product.Product')
        assert obj.pk == 1, 'Should create a Product instance'

    def test_category(self):
        obj = mixer.blend('product.Category')
        str_categories = 'pain, miel, poisson, céréales'
        obj.extract(str_categories)
        obj.create_categories()
        
        assert isinstance(obj.get_category('pain'), Category)
        assert isinstance(obj.get_category('céréales'), Category)
        assert obj.get_category('cérles') == False