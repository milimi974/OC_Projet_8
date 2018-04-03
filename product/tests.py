from django.test import TestCase

# Create your tests here.
from tools import upload_openfoodfact_cvs


class UpdateMethodTests(TestCase):

    def test_upload_csv(self):
        """ Test upload csv file """
        assert upload_openfoodfact_cvs() == True

    def test_parse_data(self):
        pass