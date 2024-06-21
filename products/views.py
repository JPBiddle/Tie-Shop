from django.shortcuts import redirect, render, reverse, get_object_or_404
from .models import Product, Colour, Category
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ProductForm

def all_products(request):
    """ Show all products """
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products':products})


def product_info(request, product_id):
    """ Get individual product for product info page """
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_info.html', {'product':product})

def colour(request, blub):
    """ Get colour for selecting via dropdown menu """
    try: 
        colour = Colour.objects.get(name=blub)
        products = Product.objects.filter(colour=colour)
        return render(request, 'products/colour.html', {'products':products, 'colour':colour})

    except:
        return redirect('products/products.html')

def category(request, plob):
    """ Get material for selecting via dropdown menu """
    try: 
        category = Category.objects.get(name=plob)
        products = Product.objects.filter(category=category)
        return render(request, 'products/category.html', {'products':products, 'category':category})

    except:
        return redirect('products/products.html')


def search(request):
    """ Search for match in users search term """
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(Q(name__contains=searched)|Q(description__contains=searched))
        return render(request, 'products/search.html', {'searched':searched, 'products':products})

    else:

        return render(request, 'products/search.html', {})

@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New product added!')
            return redirect(reverse(add_product))
        else:
            messages.error(request, 'Failed to add new product, please check form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product successfully updated!')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request, 'Product edit failed. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product has been deleted.')
    return redirect(reverse('products'))
