from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('api/menu/', MenuAPIView.as_view(), name='menu-api'),
]