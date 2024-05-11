from django.core.management.base import BaseCommand
from myshopapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Генерация клиентов и заказов."
    print("Done!")

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(
                name=f'Name{i}',
                email=f'mail{i}@mail.ru',
                phone_number=f'+7000000{i}',
                address=f'My address {i}',
            )
            client.save()
            product = Product(
                name=f'Product{i}',
                description=f'Blablablabestproduct{i}',
                price=i*1.01,
                count=3*i,
            )
            product.save()
            for j in range(1, count + 1):
                order = Order(
                    client=client,
                    total_amount=(product.price * j)
            )
                order.save()

