import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestProduct:

    def test_model(self):
        obj = mixer.blend('product.Product')
        assert obj.pk == 1, 'Should create a Product instance'
