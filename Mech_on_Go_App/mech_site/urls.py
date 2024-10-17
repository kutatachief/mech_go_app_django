from django.urls import path
from .views import index, aboutUs,contact,contactForm,login,map,mechanic,orderPage,PartsVendor,Signup
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('contact/', views.contact, name='contact'),
    path('contactForm/', views.contactForm, name='contactForm'),
    path('login/', views.login, name='login'),
    path('map/', views.map, name='map'),
    path('mechanic/', views.mechanic, name='mechanic'),
    path('orderPage/', views.orderPage, name='orderPage'),
    path('PartsVendor/', views.PartsVendor, name='PartsVendor'),
    path('Signup/', views.Signup, name='Signup'),
]




