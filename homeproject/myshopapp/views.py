from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Client


def shop(request):
    html = """
    <h1>Добро пожаловать в магазин!</h1>
    <p>Здесь пока ничего нет .....</p>
    """
    return HttpResponse(html)


#поиск клиента по id и вывод его заказов
def client_orders(request, pk):
    client = Client.objects.filter(pk=pk).first()
    response = ''
    if client:
        # Получаем все заказы клиента
        orders = client.order_set.all()
        if orders.exists():
            response += f'Заказы клиента {client.name}:\n'
            for order in orders:
                response += f'ID заказа: {order.id}, Общая сумма: {order.total_amount}, Дата оформления: {order.order_date}\n'
        else:
            response += 'У клиента нет заказов.'
    else:
        response += 'Клиент с данным ID не найден.'
    return HttpResponse(response)


#изменение имени клиента
def change_client_name(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        client = Client.objects.filter(pk=pk).first()
        if client:
            client.name = name
            client.save()
            return JsonResponse({'success': True, 'message': 'Client name successfully changed.'})
        else:
            return JsonResponse({'success': False, 'message': 'Client with the provided ID not found.'})
    else:
        return JsonResponse({'success': False, 'message': 'Request method must be POST.'})


#удаление пользователя по id
def delete_client_view(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return JsonResponse({'success': True, 'message': f'Client ID {pk} delete.'})
