from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.contrib import messages
from django.http import HttpResponseRedirect
from rest_framework import status

def handle_contact_form(request):
    # Handles the contact form logic separately flr clarity.
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Thank you for contacting us!")
        return redirect('home')
    return form

def homepage(request):
    if request.method == 'POST':
        result = handle_contact_form(request)
        if isinstance(result, HttpResponseRedirect):
            return result
        form = result
    else:
        form = ContactForm()

    context = {
        'restaurant_name': getattr(settings, 'RESTAURANT_NAME', 'My Restaurant'),
        'form': form
    }
    return render(request, 'home.html', context)

class MenuAPIView(APIView):
    def get(self, request):
        # menu_items = MenuItem.objects.filter(available=True)
        # serializer = MenuItemSerializer(menu_items, many=True)
        # return Response(serializer.data)
        menu = [
            {
                "name": "Margherita Pizza",
                "description": "Classic cheese pizza withfresh basil and tomatoes.",
                "price": 299.00
            },
            {
                "name": "Butter chicken",
                "description": "Creamy tomato-based curry with tender chicken pieces.",
                "price": 349.00
            },
            {
                "name": "Veg Chicken",
                "description": "Fragrant rice with mixed vegetables and indian spices",
                "price": 199.00
            }
        ]
        return Response(menu, status=status.HTTP_200_OK)