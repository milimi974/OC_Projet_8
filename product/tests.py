from django.test import TestCase, RequestFactory

# Create your tests here.
from tools import upload_openfoodfact_cvs


class UpdateMethodTests(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_upload_csv(self):
        """ Test upload csv file """
        assert upload_openfoodfact_cvs() == True

    def test_parse_data(self):
        pass

    def test_autocomple_product(self):
        # Create an instance of a GET request.
        request = self.factory.get('/product/autocomplete',{'terms', 'viande'})
        print(request)