from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(product='Огурец', description='Огурец', price=69.99, amount=1972)
        product.save()
        self.stdout.write(f'{product}')