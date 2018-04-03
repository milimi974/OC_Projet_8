from django.core.management.base import BaseCommand, CommandError
from product.models import Product

class Command(BaseCommand):
    help = 'Update database'

    def add_arguments(self, parser):
        parser.add_argument('--qty',  type=int)
        parser.add_argument('--upload',  type=bool)

    def handle(self, *args, **options):

        return Product.objects.update_db(qty=options['qty'],upload=options['upload'])