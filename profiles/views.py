from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from products.models import Product
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()


    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

def add_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    redirect_url = request.POST.get('redirect_url')
    if product.add_wishlist.filter(id=request.user.id).exists():
        product.add_wishlist.remove(request.user)
    else:
        product.add_wishlist.add(request.user)

    context = {
        'user': user,
        'product': product,
    }
    return redirect(redirect_url, context)
