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
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import DatabaseError

def handle_contact_form(request):
    # Handles the contact form logic separately flr clarity.
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us!")
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def home_view(request):
    return render(request, 'home.html', {
        'restaurant_name': info.name if info elsle 'My Tasty Restaurant', 
        'menu_items': menu_items
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
    try:
        menu_items = MenuItem.objects.all().values('name', 'description', 'price')
        return JsonResponse(list(menu_items), safe=False)
    except DatabaseError as db_error:
        # Handle database-specific errors
        return JsonResponse(
            {"error": "Unable to fetch menu items due to a database issue."}, status=500
        )
    except Exception as e:
        # Handle any other unexpected errors
        return JsonResponse(
            {"error": "An unecpected error occured. Please try again later."}, status=500
        )

def about_page(request):
    restaurant = RestaurantInfo.objects.first()
    if not restaurant:
        messages.warning(request, "Restaurant information not found.")
        return redirect('home')

    context = {
        'restaurant_name': restaurant.name,
        'restaurant_description': "Welcome to our cozy restaurant where we serve fresh, flavorful meals every day.",
    }
    return render(request, 'about.html', context)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

@csrf_exempt
def reservations(request):
    info = RestaurantInfo.objects.first()
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')

        if not name or not date or not time:
            return JsonResponse({'error': 'All Fields are Required.'}, status=400)

        return JsonResponse({'message': 'Reservation recevied (placeholder)'})
        
    return render(request, 'reservations.html', {
        'restaurant_name': info.name if info else 'My Tasty Restaurant',
    })