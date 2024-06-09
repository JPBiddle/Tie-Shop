from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, reverse

def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})


    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)

def adjust_cart(request, item_id):

    # Get quantity of item and add to current bag
    quantity = int(request.POST.get('quantity'))

    # get products
    if 'item_id' in request.POST:
        select = request.POST['item_id']

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))




def remove_from_cart(request, item_id):

    try:

        cart = request.session.get('cart', {})

        del cart[item_id]
        if not current_cart[item_id]:
            current_cart.pop(item_id)
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)