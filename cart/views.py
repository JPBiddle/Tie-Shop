from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, reverse
from django.contrib import messages
from products.models import Product


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    # Add quantity of product to bag
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})


    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Added {product.name} to Cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to Cart')

    request.session['cart'] = cart
    return redirect(redirect_url)

def adjust_cart(request, item_id):
    # Change quantity of product to bag
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))

    if 'item_id' in request.POST:
        select = request.POST['item_id']

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated quanity of {product.name} in Cart')
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))




def remove_from_cart(request, item_id):
    # Remove item(s) from bag
    product = Product.objects.get(pk=item_id)

    try:

        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from Cart')
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item from cart: {e}')
        return HttpResponse(status=500)