from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Cart empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51PS7N5P08fqsAAAYl3ekhMOT7TTQSnfPMoldIEtlZL64I76VDbTOW3vIc8LvRI1LVBaUnjIS0hNOtqKPp4ABaGzT00xk41Rw3o',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)