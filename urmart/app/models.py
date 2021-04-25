
from django.db import models


class Product(models.Model):

    stock_pcs = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    shop_id = models.CharField(max_length=255)
    vip = models.BooleanField()


class Order(models.Model):

    product = models.ForeignKey('app.Product', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    customer_id = models.IntegerField()
