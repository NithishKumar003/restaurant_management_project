from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm

def homepage(request):
    restaurant_name = getattr(settings, "RESTAURANT_NAME", "Restaurant")
    contact_form = ContactForm(request.POST or None)

    if request.method == 'POST' and contact_form.is_valid():
        contact_form.save()
        return redirect('homepage')

    return render(request, 'home/menu.html', {
        "restaurant_name": restaurant_name,
        "form": contact_form
    })

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
                "price": 120.00
            },
            {
                "name": "Pasta Alfredo", 
                "description": "Creamy white sauce pasta with vegetables",
                "price": 180.00
            }
        ]
        return Response(menu)
