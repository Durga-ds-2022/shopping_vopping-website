from django.shortcuts import render

# Create your views here.
def careers(request):
    return render(request, "careers.html")

def tc(request):
    return render(request, "t_c.html")

def privatepolicy(request):
    return render(request, "privatepolicy.html")

def faq(request):
    return render(request, "faq.html")

def contactus(request):
    return render(request, "contactus.html")
