from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .forms import ContactForm
from .models import MenuItem, ContactSubmission, RestaurantInfo
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

def home_view(request):
    return render(request, 'home.html', {
        'restaurant_name': getattr(settings, 'RESTAURANT_NAME', 'My Tasty Restaurant')
    })

def homepage(request):
    info = RestaurantInfo.objects.first()
    menu_items = MenuItem.objects.all()

    context = {
        'restaurant_info': info,
        'menu_items': menu_items,
    }
    return render(request, 'menu.html', context)

def contact_page(request):
    info = RestaurantInfo.objects.first()
    return render(request, 'contact.html', {'restaurant_info': info})

@api_view(['GET'])
def menu_api(request):
    items = MenuItem.objects.all()
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data)

def about_page(request):
    restaurant = get_object_or_404(RestaurantInfo, pk=1)

    context = {
        'restaurant_name': restaurant.name,
        'restaurant_description': "Welcome to our cozy restaurant where we serve fresh, flavorful meals every day.",
    }
    return render(request, 'about.html', context)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)