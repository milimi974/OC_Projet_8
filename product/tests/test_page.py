import pytest
from django.test import TestCase
from django.urls import reverse
from mixer.backend.django import mixer
from types import *

from product.models import Product

pytestmark = pytest.mark.django_db


 # Search
class SearchTestCase(TestCase):
    # test if search page return a 200
    def test_search_page(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200, 'Should be callable')

# Show
class ShowTestCase(TestCase):

    def setUp(self):
        product_qs = Product.objects.create(codebar="00112211a22atr")
        self.product = Product.objects.get(codebar="00112211a22atr")


    # test if show page return a 200 if item exist
    def test_show_page_response_200(self):

        product_id = self.product.id
        response = self.client.get(reverse('show', kwargs={'id':product_id,}))
        self.assertEqual(response.status_code, 200, 'Should be callable')

    # test if show page return a 404 if items doesn't exists
    def test_show_page_response_404(self):
        product_id = self.product.id + 1
        response = self.client.get(reverse('show', kwargs={'id':product_id,}))
        self.assertEqual(response.status_code, 404, 'Should be callable')
