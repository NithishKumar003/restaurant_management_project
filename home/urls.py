from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('menu/', menu_view, name='menu'),
]