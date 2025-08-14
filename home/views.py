from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import DatabaseError

from .forms import ContactForm, FeedbackForm
from .models import MenuItem, ContactSubmission, RestaurantInfo
from .serializers import MenuItemSerializer

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

    try:
        info = RestaurantInfo.objects.select_related("location").first()
        menu_items = MenuItem.objects.all()

        restaurant_name = info.name if info else "My Tasty Restaurant"

        location = getattr(info, "location", None)
        restaurant_address = (
            f"{location.address}, {location.city}, {location.state} - {location.zip_code}"
            if location else "Address not available"
        )

        return render(request, 'home.html', {
            'restaurant_name': restaurant_name,
            'restaurant_address': restaurant_address, 
            'menu_items': menu_items
        })

    except DatabaseError:
        messages.error(request, "Unable to load homepage due to a database issue.")
        return redirect('error_page')

def homepage(request):
    restaurant = RestaurantInfo.objects.select_related('location').first()
    menu_items = MenuItem.objects.all()

    context = {
        'restaurant_name': restaurant.name if restaurant else "My Tasty Restaurent",
        'restaurant_address': f"{restaurant.location.address}, {restaurant.location.city}, {restaurant.location.state} - {restaurant.location.zip_code}" if restaurant else "Address not available"
        'menu_items': menu_items,
    }
    return render(request, 'menu.html', context)

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Thank you! Your submission has been received.")
                return redirect('contact_page')
            except Exception as e:
                messages.error(request, "An error occurred while submitting the form please try again.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})        


@api_view(['GET'])
def menu_api(request):

    try:
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True, context={'request': request})
        return Response(serializer.data)

    except DatabaseError as db_error:
        # Handle database-specific errors
        return JsonResponse(
            {"error": "Unable to fetch menu items due to a database issue."}, status=500
        )

    except Exception as e:
        # Handle any other unexpected errors
        return JsonResponse(
            {"error": "An unexpected error occured. Please try again later."}, status=500
        )

def about_page(request):
    try:
        info = RestaurantInfo.objects.first()
        
        return render(request, 'about.html', {
            'restaurant_name': info.name if info else "My Tasty Restaurant",
            'restaurant_description': getattr(info, 'description', 'No description available.')
        })

    except DatabaseError:
        messages.error(request, "unable to load about page due to database issue.")
        return render(request, 'error.html', {
            'error_message': 'There was a problem loading the about page.'
        })

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

def feedback_page_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('feedback_page')
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})