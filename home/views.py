from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .forms import ContactForm
from .models import MenuItem, RestaurantInfo
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
    restaurant = get_object_or_404(RestaurantInfo, pk=1)

    menu_items = MenuItem.objects.all()
    form = ContactForm()

    context = {
        'restaurant_name': restaurant.name,
        'restaurant_address': restaurant.address,
        'form': form,
        'menu_items': menu_items,
    }
    return render(request, 'menu.html', context)

class MenuAPIView(APIView):
    def get(self, request):
        try:
            menu_items = MenuItem.objects.filter(available=True)
            serializer = MenuItemSerializer(menu_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # menu = [
        #     {
        #         "name": "Margherita Pizza",
        #         "description": "Classic cheese pizza withfresh basil and tomatoes.",
        #         "price": 299.00
        #     },
        #     {
        #         "name": "Butter chicken",
        #         "description": "Creamy tomato-based curry with tender chicken pieces.",
        #         "price": 349.00
        #     },
        #     {
        #         "name": "Veg Chicken",
        #         "description": "Fragrant rice with mixed vegetables and indian spices",
        #         "price": 199.00
        #     }
        # ]
        # return Response(menu, status=status.HTTP_200_OK)

def about_page(request):
    restaurant = get_object_or_404(RestaurantInfo, pk=1)

    context = {
        'restaurant_name': restaurant.name
        'restaurant_description': "Welcome to our cozy restaurant where we serve fresh, flavorful meals every day.",
    }
    return render(request, 'about.html', context)