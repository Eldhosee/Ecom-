from django.contrib import admin

from ecom.views import cart
from .models import customer, product,category,Order

admin.site.register(category)
admin.site.register(product)
admin.site.register(customer)
admin.site.register(Order)


# Register your models here.
