from django.contrib import admin

from .models import *

# Register your models here.
@ admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display  = ['id', 'first_name','last_name', 'email', 'mobile', 'age', 'gender']
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
@admin.register(ProductInOrder)
class AdminOrder(admin.ModelAdmin):
    list_display  = ['id', 'order','product', 'price']



