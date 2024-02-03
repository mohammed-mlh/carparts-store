from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Products

class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cmodels')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Submodel(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='submodels')
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Option(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    submodel = models.ForeignKey(Submodel, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    prev_price = models.FloatField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    options = models.ManyToManyField(Option, related_name='options', blank=True, null=True)
    slug = models.SlugField(default="", null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name
    
# Settings
    
class Settings(models.Model):
    active = models.BooleanField()
    main_video = models.FileField()
    whastapp = models.CharField(max_length=200)
    wechat = models.CharField(max_length=200)

    def __str__(self):
        return f'settings {self.active}'
    
# Orders
    
class Order(models.Model):
    fullname = models.CharField(max_length=3000)
    address = models.TextField()
    city = models.CharField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=30)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete= models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0, null=True)
    options = models.TextField()
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)
    