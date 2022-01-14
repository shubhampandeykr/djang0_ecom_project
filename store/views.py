from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView
from . models import Product,Category

# Create your views here.
def all_product(request):
    product = Product.objects.all()
    return render(request, 'store\home.html', {'product': product})
    
    
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store\product\single_product.html', {'product': product})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filter(category=category)
    return render(request, 'store/product/category_page.html', {'category': category, 'product': product})

