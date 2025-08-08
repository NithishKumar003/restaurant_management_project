from django.contrib import admin
from .models import MenuItem, Order, OrderItem, ContactSubmission, UserProfile, RestaurantInfo

admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ContactSubmission)
admin.site.register(UserProfile)
admin.site.register(RestaurantInfo)