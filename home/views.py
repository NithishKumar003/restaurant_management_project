from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.conf import settings

def homepage(request):
    restaurant_name = getattr(settings, "RESTAURANT_NAME", "Restaurant")
    return render(request, 'home/menu.html', {"restaurant_name": restaurant_name})

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
