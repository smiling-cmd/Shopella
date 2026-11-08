from django.contrib import admin 
from django.urls import path 
from shopapp import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('',         views.index, name='index'),

    path('services/', views.services, name='services'),

    path('register/', views.register, name='register'),





]
