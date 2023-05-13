from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.dashboard, name="dashboard"),

    # Cart views and processing
    path('products', views.productCatalog, name='products'),
    path('cart', views.shoppingCart, name='cart'),
    path('delete_cart/<int:pk>/', views.delete_cart, name = 'delete_cart'),
    path('checkout_cart', views.checkoutCart, name='checkout_cart'),
    path('confirm_order', views.confirm_order, name='confirm_order'),
    path('orders', views.userorder, name='orders'),
    path('cart_item/<uuid:pk>/', views.cart_item, name='cart_item'),

    # Profile
    path('profile', views.profile, name ='profile'),
    path('address', views.address, name ='address'),
    path('edit_address/<int:pk>/', views.editAdress, name ='edit_address'),
    path('delete_address/<int:pk>/', views.deleteAddress, name ='delete_address'),

    #login Authentication
    path('account/', include("django.contrib.auth.urls")),
    path('register', views.register, name='register'),
]