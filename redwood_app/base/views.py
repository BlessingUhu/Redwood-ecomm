from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
import sweetify
from . import models
from django.db.models import Q,F
import uuid
from django.contrib.auth import login, authenticate
from . import forms


def dashboard(request):
   return render(request, "dashboard.html")


# ----------------Cart CRUD-----------------------

def productCatalog(request):
   topics = models.ProductTopic.topics()
   allProducts = models.Products.queryFilter(request)

   # Cart Implementation

   add_to_cart = request.POST.get('prod_id')
   getProducts = models.Products
   cart_model = models.CustomerCart
   message = ""
   if(add_to_cart != None):
         getProducts = getProducts.objects.get(id = add_to_cart)
   if(request.method == 'POST'):
      try:
         cart_model.objects.get_or_create(user = request.user, product = getProducts, isOrderPlaced = False)
         cart_model.objects.filter(user = request.user, product = getProducts).update(quantity=F('quantity')+1)
         message = getProducts.name+" was added to cart successfully!"
      except cart_model.DoesNotExist:
         Http404('This item does not exist')

   context = {'topics': topics, 'allProducts': allProducts, 'cart_model':cart_model, 'message': message}
   return render(request, 'products.html', context)



@login_required(login_url='account/login')
def shoppingCart(request):
   cart_model= models.CustomerCart.objects.filter(user=request.user, isOrderPlaced = False)
   is_valid = False
   message = ""
   error = ""

   if(request.method == 'POST'):
      try:
         valid_quantity =request.POST.get('quantity_amount')
         print(valid_quantity)
         id = request.POST.get('item_id')
         if(int(valid_quantity)):
               q = cart_model.get(id = id)
               if(int(valid_quantity) > 0 and int(valid_quantity) <=10):
                  q.quantity = valid_quantity
                  q.save()
                  is_valid = True
                  message = "Quantity Updated"
               elif(int(valid_quantity) <= 0):
                  q.delete()
                  error = "Your cart is deleted"
               else:
                  error = "The quantity cannot exceed 10 and cannot be less than 0"
         else:
               error = "Quantity cannot be left empty"
      except:
         Http404("Something went wrong, please try again later")

   cart_total: int = 0
   count_quantity: int = 0
   for i in cart_model:
      if(i.isOrderPlaced == False):
         cart_total += i.total_price()
         count_quantity+=i.quantity
      else:
         i.quantity = 0
         i.save()

   context = {'cart': cart_model, 'cart_total': cart_total, 'success_message':message, "is_valid": is_valid, 'error':error, "count_quantity":count_quantity}
   return render(request, "cart.html", context)



@login_required(login_url='account/login')
def delete_cart(request, pk):
   cart_model = models.CustomerCart(id = pk)
   if(request.method == 'POST'):
      try:
         cart_model.delete()
         return redirect('/cart')
      except:
         Http404("Something went wrong, please try again later")
   return render(request, 'delete_cart.html')



@login_required(login_url='account/login')
def checkoutCart(request):
   user = request.user

   # User requests for address and defaultaddress model
   add_address = request.POST.get('add_address')
   defaultaddress_id = request.POST.get('delete_address')

   if(request.POST):
      try:
         my_model = models.DefaultAddress
         if(add_address):
            address = models.CustomerProfile.objects.get(id = add_address)
            my_model.objects.get_or_create(user = user, address = address)
         if(defaultaddress_id):
            my_model.objects.get(id = defaultaddress_id).delete()
      except:
         Http404("Something went wrong, please try again later")

   # My contexts.
   defaultaddress_model = models.DefaultAddress.objects.filter(user = user)
   all_address = models.CustomerProfile.objects.filter(user = user)
   user_cart = models.CustomerCart.objects.filter(user = user, isOrderPlaced = False)

   cart_total: float = 0.0
   count_quantity: int = 0
   sales_tax: float = 7.95

   for i in user_cart:
         cart_total += i.total_price()  
         count_quantity+=i.quantity

   context = {'all_address': all_address, 'defaultaddress_model': defaultaddress_model, 'user_cart': user_cart, 'cart_total': cart_total + sales_tax, 
   'count_quantity': count_quantity, 'sales_tax': sales_tax, 'defaultaddress_id': defaultaddress_id}
   return render(request, "checkout_cart.html", context)



@login_required(login_url='account/login')
def confirm_order(request):
   orders = models.OrdersPlaced
   cart = models.CustomerCart.objects.filter(user = request.user)

   if (request.method == "POST"):
      try:
         for items in cart:
            items.isOrderPlaced = True
            items.save()
            if(items.isOrderPlaced):
               orders.objects.get_or_create(user = request.user, cart = items)
         sweetify.success(request, 'Your order has been succesfully placed.')
         return redirect('orders')
      except:
         Http404("Something went wrong, please try again later")
   return render(request, "confirm_order.html")



@login_required(login_url='account/login')
def userorder(request):
   user = request.user
   orders = models.OrdersPlaced.objects.filter(user = user).order_by("-created")
   context = {"orders": orders}
   return render(request, "orders.html",context)



def cart_item(request, pk):
   item = models.Products.objects.get(id = pk)
   cart_model = models.CustomerCart
   message: str = ""
   if(request.method == "POST"):
         try:
            cart_model.objects.get_or_create(user = request.user, product = item, isOrderPlaced = False)
            cart_model.objects.filter(user = request.user, product = item).update(quantity=F('quantity')+1)
            message = item.name + " added to cart"
         except cart_model.DoesNotExist:
            Http404("Something went wrong, please try again")
   

   context = {"message": message, "item": item}
   return render(request, "cart_item.html", context)




# ----------User profile-----------

@login_required(login_url='account/login')
def profile(request):
   profileForm = forms.ProfileForm
   message = ""
   valid = bool
   if(request.method == 'POST'):
      profileForm = forms.ProfileForm(request.POST or None)
      if(profileForm.is_valid()):
         user = request.user
         name = profileForm.cleaned_data['name']
         address = profileForm.cleaned_data['address']
         phone = profileForm.cleaned_data['phone']
         state = profileForm.cleaned_data['state']
         country = profileForm.cleaned_data['country']
         zipcode = profileForm.cleaned_data['zipcode']
         message = "Address added successfully."
         valid = profileForm.is_valid()
         model = models.CustomerProfile(user=user, name=name, address=address, phone=phone, state=state, country=country, zipcode=zipcode)
         model.save()
   context = {'forms': profileForm, 'message': message, 'formvalid': valid}
   return render(request, 'profile.html', context)




@login_required(login_url='account/login')
def address(request):
   profile = models.CustomerProfile.objects.filter(user=request.user)
   context = {'profile': profile, 'profileCount': profile.count()}

   return render(request, 'address.html',context)


@login_required(login_url='account/login')
def editAdress(request, pk):
   profile = models.CustomerProfile.objects.filter(user=request.user).get(id = pk)
   message = ""
   valid = bool
   form = forms.ProfileForm(instance=profile)
   if request.method == 'POST':
      form = forms.ProfileForm(request.POST, instance=profile)
      if(form.is_valid()):
         form.save()
         valid = form.is_valid()
         message = "Address successfully updated."
   context= {"forms": form, 'message': message, 'formvalid': valid}

   return render(request, "edit_address.html", context)



@login_required(login_url='account/login')
def deleteAddress(request, pk):
   profile = models.CustomerProfile.objects.filter(user=request.user).get(id = pk)
   if(request.method == 'POST'):
      profile.delete()
      return redirect('address')
   return render(request, "delete_address.html")





#--------Login VIEWS-----------

def register(request):
   form = forms.CustomUserCreationForm
   if(request.method == 'GET'):
      return render(request, 'registration/register.html', {'form': form})

   elif (request.method == 'POST'):
      form = form(request.POST or None)
      if(form.is_valid()):
         user = authenticate(request.POST)
         form.save()
         login(request, user)
         return redirect('login')
   context = {'form': form, 'formchanged': form.has_changed()}
   return render(request, 'registration/register.html', context)


