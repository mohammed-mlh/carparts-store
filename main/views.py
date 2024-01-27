from django.shortcuts import render
from .models import Brand, Model, Submodel, Product

def index(request):
    brands = Brand.objects.all()
    return render(request, 'pages/index.html', {'brands': brands})

def brand(request, brand):
    models = Brand.objects.get(name=brand).cmodels.all()
    return render(request, 'pages/brand.html', {'models': models, 'brand': brand})

def model(request, brand, model):
    submodels = Model.objects.get(name=model).submodels.all()
    return render(request, 'pages/model.html', {'submodels': submodels, 'brand': brand, 'model': model})

def submodel(request, brand, model, submodel):
    products = Submodel.objects.get(name=submodel).products.all()
    return render(request, 'pages/submodel.html', {'products': products, 'brand': brand, 'model': model, 'submodel': submodel})