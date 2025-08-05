from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('api/menu/', MenuAPIView.as_view(), name='menu-api'),
]