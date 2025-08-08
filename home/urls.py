from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('api/menu/', views.menu_api, name='menu-api'),
    path('about/', views.about_page, name='about'),
]