from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from django.conf import settings
from .models import MenuItem
from .serializers import MenuItemSerializer

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
        menu_items = MenuItem.objects.filter(available=True)
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)
