from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from django.conf import settings
from .models import MenuItem
from .serializers import MenuItemSerializer

def homepage(request):
    menu = MenuItem.objects.filter(available=True)
    contact_form = ContactForm()

    return render(request, 'home.html', {
        'menu': menu,,
        'restaurant_name': getattr(settings, 'RESTAURANT_NAME', 'My Restaurant'),
        'address': '123 Main Street, Chennai, India', 
        'form': contact_form,
    })

class MenuAPIView(APIView):
    def get(self, request):
        menu_items = MenuItem.objects.filter(available=True)
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)
