from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand, Model, Submodel, Product, Settings
from django.views.decorators.csrf import csrf_exempt

# Simple Page
def index(request):
    settings = Settings.objects.first()
    return render(request, 'pages/index.html', {'settings': settings})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

# HTMX Components

@csrf_exempt
def brands(request):
  brands = Brand.objects.all()
  return render(request, 'partials/brands.html', {'brands': brands})

@csrf_exempt
def models(request, brand):
  models = Brand.objects.get(name=brand).cmodels.all()
  return render(request, 'partials/models.html', {
     'brand': brand,
     'models': models
  })


# Indexed Products and Product

def indexed_products(request, brand, model):
    products_by_submodels = []
    submodels = Model.objects.get(name=model).submodels.all()
    for submodel in submodels:
      products_by_submodels.append({
        'submodel': submodel.name,
        'products': submodel.products.all()
      })
    print(products_by_submodels)
    return render(request, 'pages/indexed_products.html', {'products_by_submodels': products_by_submodels, 'brand': brand, 'model': model})

def product(request, slug):
    product = Product.objects.get(slug=slug)
    related_products = Product.objects.filter(submodel = product.submodel)
    context = {'product': product, 'related_products':related_products}
    print(product.options.all())
    return render(request, 'pages/product.html', context)
