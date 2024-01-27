from django.urls import path
from . import views

# app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('q', views.index, name='index'),
    path('q/<str:brand>', views.brand, name='brand'),
    path('q/<str:brand>/<str:model>', views.model, name='model'),
    path('q/<str:brand>/<str:model>/<str:submodel>', views.submodel, name='submodel'),
]