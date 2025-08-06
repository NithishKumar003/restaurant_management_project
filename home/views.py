from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from .models import MenuItem
from .serializers import MenuItemSerializer

def homepage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us!")
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'restaurant_name': getattr(settings, 'RESTAURANT_NAME', 'My Restaurant'),
        'form': form
    }
    return render(request, 'home.html', context)

class MenuAPIView(APIView):
    def get(self, request):
        menu_items = MenuItem.objects.filter(available=True)
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)
