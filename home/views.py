from django.shortcuts import render
import requests
from .models import MenuItem

def homepage(request):
    return render(request, 'home/menu.html')

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'home/menu.html', {'menu_items': menu_items})

class MenuAPIView(APIView):
    def get(self, request):
        menu = [
            {
                "name":"Margherita Pizza",
                "description": "Classic cheese and tomato pizza",
                "price":250.00
            },
            {
                "name": "Veg burger",
                "description": "Loaded veg patty with lettuce and tomato",
                "prive": 120.00
            },
            {
                "name": "Pasta Alfredo", 
                "description": "Creamy white sauce pasta with vegetables",
                "price": "180.00"
            }
        ]
        return Response(menu)
