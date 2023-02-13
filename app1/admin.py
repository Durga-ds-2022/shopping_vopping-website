from django.contrib import admin
from .models import Categories,Product, ProImage
# Register your models here.

# admin.site.register(Categories)
# admin.site.register(Product)
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display  = ['id', 'name','category', 'price', 'discount_price']
admin.site.register(ProImage)



