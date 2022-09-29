from email.mime import image
from django.shortcuts import redirect, render
from .models import category,product,customer,Order
from django.contrib.auth import authenticate ,login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password,check_password
from .form import add_to_cart
from .middleware.auth import auth_middleware
from django.utils.decorators import method_decorator

# Create your views here.

def index(request):
    
    user_id=request.session.get('user_id')
    return render(request,"ecom/index.html",{
        "user_id":user_id
    })


def logout(request):
    request.session.clear()
    user_id=request.session.get('user_id')
    return redirect('login')


def register(request):
    
   
    if request.method=='POST':
        password1=request.POST['password']
        username=request.POST['email']
        if username:
            new_user=customer(
        
            username=username,
            password=make_password(password1)
        
            )
            if new_user.isExists():
                error_message="user already exists"
                return render (request,'ecom/register.html',{
                "error":error_message
            })



            else:
                new_user.save()
    
            return redirect('login')
        

    return render (request,'ecom/register.html')



def collections(request):
    collections=category.objects.filter(status=0)
    
    collections_id=request.GET.get('collections')
    product_id=request.GET.get('product')
    
    if collections_id:
        collection_product=product.get_all_category_product(collections_id)
        return render(request,"ecom/category_list.html",{
            "category_list":collection_product
        })
    elif product_id:
        product_view=product.get_all_category_product_data(product_id)
        return render(request,"ecom/productpage.html",{
            "product":product_view,
            
        })

    else:


        return render(request,"ecom/collections.html",{
            "collection":collections

    })





    # login
def login(request):
   
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        try:
            user=customer.objects.get(username=username)
        except:
            
            message="Invalid user"
            return render(request,"ecom/login.html",{
                "error":message
            })

        
        if user:
            check_pass=check_password(password,user.password)
            if check_pass:
                request.session['user_id']=user.id
                
                return render(request,"ecom/index.html",{
                    "user":user,     
                    "user_id":user               
                })
            else:
                message="Invalid password"
                return render(request,"ecom/login.html",{
                "error":message
            })

       
    return render(request,"ecom/login.html")


@auth_middleware
def add_to_cart(request):
    
    if request.method=='POST':
        product_id=request.POST.get('product_id')
        quantity=request.POST.get('quantity')
        try:
            quantity=int(quantity)
        except:
            quantity=1

        
        product_view=product.get_all_category_product_data(product_id)
            
        cart=request.session.get("cart")
        
        if cart:
            cart[product_id]=quantity
        else:
            cart={}
            cart[product_id]=1
          
    request.session['cart']=cart
    
    return render(request,"ecom/productpage.html",{
        "product":product_view,
        "quantity":quantity
    })
    
@auth_middleware
def cart(request):
    if request.method=='POST':
     try:
        product_id=request.POST.get("product_id")
        cart = request.session.get('cart')
        if product_id:
           
            cart.pop(product_id)
        request.session['cart']=cart
        ids = request.session.get('cart')
            
            
            
        products=product.get_all_cart_product(ids)
        return render(request,"ecom/cart.html",{
        "product":products
         
    })
     except:
        ids = request.session.get('cart')
            
        products=product.get_all_cart_product(ids)
        
        return render(request,"ecom/cart.html",{
        "product":products
         
    })
    
    



    if request.method=='GET':

        try:
            ids=list(request.session.get('cart').keys())
            
            products=product.get_all_cart_product(ids)
            return render(request,"ecom/cart.html",{
        "product":products
         
    })
        except:
            return render(request,"ecom/cart.html",{
                
        
         
    })

def address(request):
    if request.method=='GET':
        return render(request,"ecom/address.html")

def payment(request):
    if request.method=='POST':
        address=request.POST.get('address')
        phone_number=request.POST.get('number')
        
        if address:
            if phone_number:
                return render(request,"ecom/payment.html",{
            "address":address,
            "phone":phone_number
        })
            else:
                return render(request,"ecom/address.html",{
                    "input":"phone number"
                })
        else:
            return render(request,"ecom/address.html",{
                    "input":"address"
                })
    
    return render(request,"ecom/payment.html")



@auth_middleware
def checkout(request):
    if request.method=='GET':
        customers=request.session.get('user_id')
        order_items=Order.order_items(customers)
        user=customer.objects.filter(id=customers)
        sum=0
    
        for i in order_items:
            a=i.quantity*i.price
            sum+=a

    
        return render(request,"ecom/checkout.html",{
        "customer":user,
        "order":order_items,
        "total_price":sum,
        
        })


    if request.method=='POST':
       card_number=request.POST.get('card_number')
       card_name=request.POST.get('card_name')
       expiration=request.POST.get('expiration')
       cvv=request.POST.get('cvv')
       if  card_number:
           if card_name:
               if expiration:
                   if cvv:
                       pass
                   else:
                       return redirect('payment')
               else:
                   return redirect('payment')
           else:
                return redirect('payment')                
       else:
                return redirect('payment')  

       address=request.POST.get('address')
       phone_number=request.POST.get('number')
       a=request.session.get('cart')
    
       ids=a.keys()
       products=product.get_all_cart_product(ids)
       items=list(products)
      
       customers=request.session.get('user_id')
       user=customer.objects.filter(id=customers)
       
       
       for item in items:
           
                order = Order(customer=customer(id=customers),
                          product=item,
                          price=item.selling_price,
                          quantity=a.get(str(item.id)),
                          address=address,
                          phone=phone_number,
                          

                          )
                order.save()
       request.session['cart']={}
    order_items=Order.order_items(customers).reverse()
    sum=0
    
    for i in order_items:
        a=i.quantity*i.price
        sum+=a

    
    return render(request,"ecom/checkout.html",{
        "customer":user,
        "order":order_items,
        "total_price":sum,
        "address":address,
        "phone":phone_number
    })


        
      

   



