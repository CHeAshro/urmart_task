
from django.test import TestCase
from django.urls import reverse

from app.models import Order, Product
from app.forms import CreateOrderForm


class TestOrderView(TestCase):
    def setUp(self):
        super().setUp()

        self.url = reverse('app:view-order')

        product_1 = Product.objects.create(stock_pcs=20, price=100, shop_id='shop_1', vip=True)
        product_2 = Product.objects.create(stock_pcs=30, price=200, shop_id='shop_2', vip=False)

        Order.objects.create(product=product_1, qty=2, customer_id=1)
        Order.objects.create(product=product_2, qty=4, customer_id=2)

    def test_get(self):
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)

        self.assertIsInstance(CreateOrderForm, response.context['create_order_form'])
        self.assertQuerysetEqual(Product.objects.all(), response.context['product_list'])
        self.assertQuerysetEqual(Order.objects.all(), response.context['order_list'])
