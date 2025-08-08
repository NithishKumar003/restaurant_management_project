from django.urls import path
from .views import *

urlpatterns = [
    path('', views.home_view, name='homeview')
    path('menu/', views.homepage, name='home'),
    path('api/menu/', views.menu_api, name='menu-api'),
    path('about/', views.about_page, name='about'),
    path('contact/' views.contact_page, name='contact')
]