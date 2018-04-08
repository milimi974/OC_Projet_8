import pytest
from django.test import TestCase
from django.urls import reverse
from mixer.backend.django import mixer
from types import *
from django.contrib.auth.models import User

pytestmark = pytest.mark.django_db


 # Login
class LoginTestCase(TestCase):
    # test if login page return 200
    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200, 'Should be callable')

# Register
class RegisterTestCase(TestCase):
    # test if Mention legal page return 200
    def test_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200, 'Should be callable')

# Profile
class ProfileTestCase(TestCase):
    # test if Mention legal page return 200
    def test_profile_page(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200, 'Should be callable')

# User product list
class UserProductTestCase(TestCase):
    # test if User product list page return 200 if user login
    def test_user_product_page_return_200(self):
        user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
        self.client.login(username='foo', password='bar')
        response = self.client.get(reverse('substitution'))
        self.assertEqual(response.status_code, 200, 'Should be callable')


    # test if User product list page return 302 if user isn't login
    def test_user_product_page_return_302(self):
        response = self.client.get(reverse('substitution'))
        self.assertEqual(response.status_code, 302, 'Should be callable')