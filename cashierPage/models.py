from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=150, null=True, blank=True, unique=True)
    code_product = models.CharField(max_length=100, null=True, unique=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    price_buy = models.FloatField(null=True, blank=True)
    price_sale = models.FloatField( blank=True, null=True)
    discription = models.TextField(null=True, blank=True)
    date_buy = models.DateField(auto_now_add=True,null=True, blank=True)
    sale_deadline = models.DateField(null=True, blank=True)
    
    #z = 'abcdefghijklmnopgrstuvwxyz'
    def save(self, *args, **kwargs):
        if not self.code_product:
            self.code_product = self.code + "Prd00" + self.name
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})
        return reverse("home")
    
    def __str__ (self):
        return str(self.code_product) + " | " + str(self.name)
    
class pra_checkOut(models.Model):
    code = models.CharField(max_length=255, null=True, blank=True)
    Product = models.ManyToManyField(Product,null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    date = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.code)
    
    
class checkOut(models.Model):
    code = models.CharField(max_length=255, null=True, blank=True)
    product = models.ForeignKey(pra_checkOut,blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.code)
    

