from django.contrib import admin 
from django.urls import path 
from shopapp import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('about/', views.about),

    path('contact/', views.contact),

    path('index/', views.index),

    path('index/', views.services),





]
