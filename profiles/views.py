from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

@login_required
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

@login_required
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

@login_required
def wishlist(request):
#Display wishlist
    product = Product.objects.filter(favourited_by=request.user.userprofile)

    return render(request, 'profiles/wishlist.html', {"wishlist":product})

@login_required
def remove_wishlist(request, id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
#Remove product from wishlist
    remove = get_object_or_404(Product, id=id)
    product = Product.objects.filter(favourited_by=request.user.userprofile)
    remove.favourited_by.remove(request.user.userprofile)
    messages.success(request, (
            f'Removed { remove.name } from favourites!'
        ))
    return render(request, 'profiles/wishlist.html', {"wishlist":product})

@login_required
def add_wishlist(request, id):
#Add product to wishlist
    product = get_object_or_404(Product, id=id)
    if product.favourited_by.filter(id=request.user.id).exists():
        product.favourited_by.remove(request.user.userprofile)
    else:
        product.favourited_by.add(request.user.userprofile)
        messages.success(request, (
            f'{ product.name } is in your favourites!'
        ))
    return render(request, 'products/product_info.html', {'product':product})

def details(request, product_id):
#For product detail button in wish list
    product = get_object_or_404(Product, id=id)

    return render(request, 'products/product_info.html', {'product':product})
