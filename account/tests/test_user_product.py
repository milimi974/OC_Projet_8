import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer

from account.views import save
from django.contrib.auth.models import AnonymousUser, User

pytestmark = pytest.mark.django_db

from ..models import *

class TestUserProduct:

    def test_save(self):
        params = {'id': 347, 'sub_id': 1073}
        # create instance of pos request
        req = RequestFactory().post('/account/save', params)
        req.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

        response = save(req)
        assert response.status_code == 200, 'Should be callable'