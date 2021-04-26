
from django.shortcuts import redirect, render

from app.forms import CreateOrderForm
from app.models import Product, Order


def order_view(request):

    create_order_form = CreateOrderForm()
    product_list = Product.objects.all()
    order_list = Order.objects.select_related('product')

    context = {
        'create_order_form': create_order_form,
        'product_list': product_list,
        'order_list': order_list
    }

    return render(request, 'views.html', context)
