from django.core.management.base import BaseCommand
from myapp.models import Order, Client, Product


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        ex_client = Client.objects.get(pk=2)
        chosen_product = Product.objects.get(product='Огурец')
        order = Order(client=ex_client, summ=209.97)
        order.save()
        order.product.set([chosen_product])
        self.stdout.write(f'{order}')
