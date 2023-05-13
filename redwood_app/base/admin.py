from django.contrib import admin
from . import models;

# Register your models here.

admin.site.register(models.ProductTopic)
admin.site.register(models.Products)
admin.site.register(models.CustomerProfile)
admin.site.register(models.CustomerCart)
admin.site.register(models.DefaultAddress)
admin.site.register(models.OrdersPlaced)