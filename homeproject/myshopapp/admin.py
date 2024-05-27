from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description="Сбросить количество на ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count']
    actions = [reset_quantity]
    search_help_text = 'Поиск по названию продукта'
    search_fields = ['name']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    search_help_text = 'Поиск по имени'
    search_fields = ['name']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Контакты',
            {
                'description': 'Контактная информация клиента',
                'fields': ['email', 'phone_number', 'address'],

            },
        ),
        (
            'Дата добавления клиента',
            {
                'classes': ['collapse'],
                'fields': ['registration_date'],
            }
        ),
    ]



class OrderAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'total_amount', 'order_date']
    ordering = ['-total_amount']
    search_help_text = 'Поиск по имени клиента, по наименованию продукта'
    search_fields = ['client__name', 'products__name']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'Список заказанных продуктов',
            {
                'fields': ['products'],

            },
        ),
        (
            'Сумма заказа',
            {
                'fields': ['total_amount'],
            }
        ),
    ]

    def client_name(self, obj):
        return obj.client.name


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
