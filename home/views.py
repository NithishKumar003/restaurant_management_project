from django.shortcuts import render
import requests
from .models import MenuItem

def homepage(request):
    return render(request, 'home/menu.html')

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'home/menu.html', {'menu_items': menu_items})
