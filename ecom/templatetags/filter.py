
from django import template

register = template.Library()

@register.filter(name="get_product_quantity_in_cart")
def get_product_quantity_in_cart(product,cart):
    ids=cart.keys()
    for i in ids:
       if int(i) ==product.id:
         return cart.get(i)


@register.filter(name="get_total_price")
def get_total_price(product,cart):
    return product.selling_price * get_product_quantity_in_cart(product , cart)


@register.filter(name="total_cart_price")
def total_cart_price(products , cart):
    sum = 0 
    for p in products:
        sum += get_total_price(p , cart)

    return sum

@register.filter(name="get_price")
def get_price(number1,number):
    return number1*number



    
        