from django.urls import path
from ecom import views
from .middleware.auth import auth_middleware


urlpatterns=[
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('collections/',views.collections,name="collections"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('add_to_cart',views.add_to_cart,name="add_to_cart"),
    path('cart',views.cart,name="cart"),
    path('payment',views.payment,name="payment"),
    path('checkout',views.checkout,name="checkout"),
    path('address',views.address,name="address"),
    
    
    
]