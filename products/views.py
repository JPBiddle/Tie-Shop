from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Colour

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
        return render(request, 'products/colour.html', {'products':products})


    except:
        return redirect('products/products.html')

