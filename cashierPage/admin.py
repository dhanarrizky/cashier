from django.contrib import admin
from .models import Product, pra_checkOut, checkOut


# Register your models here.
admin.site.register(Product)
admin.site.register(pra_checkOut)
admin.site.register(checkOut)