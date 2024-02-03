from django.urls import path
from . import views

# app_name = 'polls'
urlpatterns = [
    path('', views.index, name='brand'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('q', views.brands, name="brands"),
    path('q/<str:brand>', views.models, name='models'),
    path('q/<str:brand>/<str:model>', views.indexed_products, name='indexed_products'),
    # path('q/<str:brand>/<str:model>/<str:submodel>', views.submodel, name='submodel'),

    path('product/<slug:slug>', views.product, name='product-detail'),
]