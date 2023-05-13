from django.db import models
import uuid
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.


    # ----------- Product Topic Model------------------#
class ProductTopic(models.Model):
    name = models.CharField(max_length=100, null=False)
    
    def __str__(self) -> str:
        return self.name
    def topics():
        return ProductTopic.objects.all()


    # ----------- Product Model------------------#
class Products(models.Model):
    name = models.CharField(max_length=150)
    description= models.TextField(max_length=300, null=False)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    topic = models.ForeignKey(ProductTopic, on_delete=models.CASCADE, default=None)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    def queryFilter(request):
        q = request.GET.get('q')
        if(q != None):
            allProducts = Products.objects.all().order_by('-topic__name').filter(topic__name__icontains = q)
        else:
            allProducts = Products.objects.all().order_by('-topic__name')
        return allProducts


    # ----------- Product Profile ------------------#
class CustomerProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = PhoneNumberField(blank=True)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.state


    # ----------- Customer's Cart ------------------#
class CustomerCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0, message="Product is no more available"), MaxValueValidator(10)])
    isOrderPlaced = models.BooleanField(default=False)


    def total_price(self) -> int:
        return self.product.price * self.quantity
    
    def cart_id(self) -> int:
        return self.id

    def __str__(self) -> str:
        return self.product.name



    # ----------- Chosen Address for checkout ------------------#
class DefaultAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    address = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, default=None)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __uuid__(self):
        return self.id


    # ----------- Orders placed ------------------#
class OrdersPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    cart = models.ForeignKey(CustomerCart, on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __uuid__(self):
        return self.id