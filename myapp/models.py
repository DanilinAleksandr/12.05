from django.db import models
from datetime import datetime


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=120)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Phone: {self.phone}'


class Product(models.Model):
    product = models.CharField(max_length=80)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    additional_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return f'Product: {self.product}, Price: {self.price}, Amount: {self.amount}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    summ = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(default=datetime(year=2024, month=5, day=11))

    def __str__(self):
        return f'Client: {self.client}, Summ: {self.summ}, Order date: {self.order_date}'
