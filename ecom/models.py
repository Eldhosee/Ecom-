
from django.db import models
from django.forms import ImageField

class category(models.Model):
    
    name=models.CharField(max_length=30,null=False,blank=False)
    image=models.CharField(max_length=1000)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return  f"{self.id} :{self.name}" 



class product(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
   
    name=models.CharField(max_length=30,null=False,blank=False)
    image=models.CharField(max_length=1000)
    description=models.TextField(max_length=2000,blank=False )  
    
    
    selling_price=models.FloatField(null=False,blank=False)
    orginal_price=models.FloatField(null=False,blank=False)

    
    

   


    @staticmethod
    def get_all_category_product(category_id):
        return product.objects.filter(category=category_id)
    @staticmethod
    def get_all_category_product_data(product_id):
        return product.objects.filter(id=product_id)
    
    @staticmethod
    def get_all_cart_product(ids):
        return product.objects.filter(id__in=ids)
    
 
        
    



   
   

class customer(models.Model):
    username=models.CharField(max_length=30,null=False,blank=False)
    password=models.CharField(max_length=1000,null=False,blank=False)
    def __str__(self):
        return  f"{self.id} :{self.username}" 
    def isExists(self):
        if customer.objects.filter(username=self.username):
            return True
        else:
            return False

class Order(models.Model):
    product = models.ForeignKey(product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    
    status = models.BooleanField(default=False)
    
    def order_items(customer_id):
        return Order.objects.filter(customer=customer_id)
    
    

 






