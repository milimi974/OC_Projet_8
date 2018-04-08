import pytest
from django.test import TestCase
from mixer.backend.django import mixer
from types import *
from product.models import Category, Product
from django.core import management

pytestmark = pytest.mark.django_db


 # Update Product
class UpdateProductTestCase(TestCase):


    # test that a new product is made
    def test_new_product_is_made(self):
        response = management.call_command('updateproducts', qty=1, upload=False)
        self.assertEqual(response, 'Total entry : 1')
        response = management.call_command('updateproducts', qty=510, upload=False)
        self.assertEqual(response, 'Total entry : 510')
        response = management.call_command('updateproducts', qty=1050, upload=False)
        self.assertEqual(response, 'Total entry : 1050')

