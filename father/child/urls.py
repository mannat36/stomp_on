from django.urls import path
from . import views

urlpatterns = [
    path('child/',views.child,name='child'),
    path('home/', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact')
]

