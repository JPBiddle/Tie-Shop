from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import generic

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
        else:
            messages.error(request, 'Error updating profile, please ensure form is valid.')
    else:
        form = UserProfileForm(request.POST, instance=profile)
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

# Add items to wishlist - credit for help: https://www.youtube.com/watch?v=OgA0TTKAtqQ&t=2420s

def wishlist(request):
    product = Product.objects.filter(wished_item=request.user.userprofile)

    return render(request, 'profiles/wishlist.html', {"wishlist":product})

def remove_wishlist(request, id):
    remove = get_object_or_404(Product, id=id)
    product = Product.objects.filter(wished_item=request.user.userprofile)
    remove.wished_item.remove(request.user.userprofile)
    messages.success(request, (
            f'Removed { remove.name } from favourites!'
        ))
    return render(request, 'profiles/wishlist.html', {"wishlist":product})

def add_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.wished_item.filter(id=request.user.id).exists():
        product.wished_item.remove(request.user.userprofile)
    else:
        product.wished_item.add(request.user.userprofile)
        messages.success(request, (
            f'{ product.name } is in your favourites!'
        ))
    return render(request, 'products/product_info.html', {'product':product})
