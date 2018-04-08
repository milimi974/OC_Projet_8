import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from types import *


from django.test import TestCase

pytestmark = pytest.mark.django_db


#  Homepage
class HomePageTestCase(TestCase):
    # test if home page return 200
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200, 'Should be callable')

# Mention legal
class MentionLegalTestCase(TestCase):
    # test if Mention legal page return 200
    def test_mention_legal_page(self):
        response = self.client.get(reverse('mentions'))
        self.assertEqual(response.status_code, 200, 'Should be callable')