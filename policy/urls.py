from django.urls import path
from . import views
urlpatterns = [
    
    path("careers/",views.careers,name='careers'),
    path("tc/",views.tc,name='tc'),
    path("privatepolicy/",views.privatepolicy,name='privatepolicy'),
    path("faq/",views.faq,name='faq'),
    path("contactus/",views.contactus,name='contactus'),
    
]