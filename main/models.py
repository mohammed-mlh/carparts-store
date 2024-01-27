from django.db import models

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
    
class Product(models.Model):
    submodel = models.ForeignKey(Submodel, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    prev_price = models.FloatField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name