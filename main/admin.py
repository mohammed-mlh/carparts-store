from django.contrib import admin
from main.models import Brand, Model, Submodel, Product

admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Submodel)
admin.site.register(Product)