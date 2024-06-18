from django.shortcuts import redirect, render, reverse, get_object_or_404
from .models import Product, Colour, Category
from django.db.models import Q
from django.contrib import messages

from .forms import ProductForm

def all_products(request):

    products = Product.objects.all()
    return render(request, 'products/products.html', {'products':products})


def product_info(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/product_info.html', {'product':product})

def colour(request, blub):

    try: 
        colour = Colour.objects.get(name=blub)
        products = Product.objects.filter(colour=colour)
        return render(request, 'products/colour.html', {'products':products, 'colour':colour})


    except:
        return redirect('products/products.html')

def category(request, plob):

    try: 
        category = Category.objects.get(name=plob)
        products = Product.objects.filter(category=category)
        return render(request, 'products/category.html', {'products':products, 'category':category})


    except:
        return redirect('products/products.html')


def search(request):

    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(Q(name__contains=searched)|Q(description__contains=searched))
        return render(request, 'products/search.html', {'searched':searched, 'products':products})

    else:

        return render(request, 'products/search.html', {})

def add_product(request):
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