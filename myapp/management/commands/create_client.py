from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='Nam', email='noname@mail.ru', phone='+79091237766', address='SPB')
        client.save()
        self.stdout.write(f'{client}')
