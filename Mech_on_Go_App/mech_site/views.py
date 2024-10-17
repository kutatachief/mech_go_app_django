from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mech_site/index.html')

def aboutUs(request):
    return render(request, 'mech_site/aboutUs.html')

def contact(request):
    return render(request, 'mech_site/Contact.html')

def contactForm(request):
    return render(request, 'mech_site/ContactForm.html')

def login(request):
    return render(request, 'mech_site/login.html')

def map(request):
    return render(request, 'mech_site/map.html')

def mechanic(request):
    return render(request, 'mech_site/mechanic.html')

def orderPage(request):
    return render(request, 'mech_site/orderPage.html')

def PartsVendor(request):
    return render(request, 'mech_site/PartsVendor.html')

def Signup(request):
    return render(request, 'mech_site/Signup.html')
