from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Categories(models.TextChoices):
    Men = "Men"
    Women = "Women"
    Jewellery = "Jewellery"
    Kids="Kids"
    Sportswear="Sportswear"


class Product(models.Model):
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=20,choices=Categories.choices)
    price = models.FloatField()
    discount_price=models.IntegerField(default=0)
    is_top5=models.BooleanField(default=False)
    #description=models.TextField(blank=True, null=True)
    Details=RichTextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class ProImage(models.Model):
    
    image=models.ImageField(upload_to=None)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productimage")    
    
    def __str__(self):
        return self.product.name

        