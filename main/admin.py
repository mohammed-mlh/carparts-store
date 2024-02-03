from django.contrib import admin
from main.models import Brand, Model, Submodel, Product, Option, Settings, Order, OrderItem


class OrdersItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['fullname','address', 'city', 'phone_number', 'complete']}),
    ]
    inlines = [OrdersItemInline]

admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Submodel)
admin.site.register(Product)
admin.site.register(Option)

admin.site.register(Settings)

admin.site.register(Order, OrderAdmin)
