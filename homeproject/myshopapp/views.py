from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse
from django.http import JsonResponse

from .forms import ProductForm
from .models import Client, Product


def shop(request):
    return render(request, 'myshopapp/shop_main.html')


# все клиенты
def all_clients(request):
    clients = Client.objects.all()
    return render(request, 'myshopapp/all_clients.html', {'clients': clients})


# #поиск клиента по id и вывод его заказов
def client_orders_view(request, pk):
    client = Client.objects.filter(pk=pk).first()
    if client is None:
        return render(request, 'myshopapp/client_orders.html', {'error_message': 'Клиент не найден.'})

    orders = client.order_set.all()  # Получаем все заказы клиента
    return render(request, 'myshopapp/client_orders.html', {'client': client, 'orders': orders})


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


# сортировка по времени
def ordered_products(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return render(request, 'myshopapp/ordered_products.html', {'error': 'Клиент с данным ID не найден.'})

    now = timezone.now()
    last_week = now - timedelta(days=7)
    last_month = now - timedelta(days=30)
    last_year = now - timedelta(days=365)

    orders_week = client.order_set.filter(order_date__gte=last_week)
    orders_month = client.order_set.filter(order_date__gte=last_month)
    orders_year = client.order_set.filter(order_date__gte=last_year)

    context = {
        'client': client,
        'orders_week': orders_week,
        'orders_month': orders_month,
        'orders_year': orders_year,
    }

    return render(request, 'myshopapp/ordered_products.html', context)


#создание нового товара
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            form.save()
            message = 'Пользователь сохранён'
            return redirect('all_products')
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'myshopapp/add_product.html', {'form': form, 'message': message})


#изменение продукта
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('all_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'myshopapp/edit_product.html', {'form': form, 'product': product})

#все продукты
def all_products(request):
    products = Product.objects.all()
    return render(request, 'myshopapp/all_products.html', {'products': products})
