from django.core.management.base import BaseCommand
from myshopapp.models import Client, Order


class Command(BaseCommand):
    help = "Поиск клиента по id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{client}')
        if client:
            # Получаем все заказы клиента
            orders = client.order_set.all()
            if orders.exists():
                self.stdout.write(f'Заказы клиента:')
                for order in orders:
                    self.stdout.write(
                        f'ID заказа: {order.id}, Общая сумма: {order.total_amount}, Дата оформления: {order.order_date}')
            else:
                self.stdout.write('У клиента нет заказов.')
        else:
            self.stdout.write('Клиент с данным ID не найден.')
