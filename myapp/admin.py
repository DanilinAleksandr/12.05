from django.contrib import admin
from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    """Список клиентов"""
    list_display = ['id', 'name', 'email', 'phone', 'address', 'register_date']
    ordering = ['id']
    list_filter = ['address', 'register_date']

    """Клиент"""
    readonly_fields = ['id', 'name', 'email', 'phone', 'address', 'register_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['id', 'name'],
            },
        ),
        (
            'Информация о клиенте',
            {
                'fields': ['email', 'phone', 'address', 'register_date'],
            }
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    """Список товаров"""
    list_display = ['id', 'product', 'description', 'price', 'amount', 'additional_date', 'image']
    ordering = ['id']
    list_filter = ['product', 'amount']
    search_fields = ['description']
    search_help_text = 'Поиск по описанию продукта'

    """Товар"""
    readonly_fields = ['id', 'additional_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['id', 'product'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Описание',
                'fields': ['description', 'additional_date', 'image'],
            }
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'amount'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    """Список заказов"""
    list_display = ['id', 'client', 'summ', 'order_date']
    ordering = ['id']
    list_filter = ['client', 'product', 'order_date']

    """Заказ"""
    readonly_fields = ['id', 'client', 'product', 'summ', 'order_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['id', 'client'],
            },
        ),
        (
            'Информация о заказе',
            {
                'fields': ['product', 'summ', 'order_date'],
            }
        ),
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
