from django.contrib import admin
from .models import MenuItem, Order, OrderItem, ContactSubmission, UserProfile, RestaurantInfo, RestaurantLocation

admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ContactSubmission)
admin.site.register(UserProfile)
admin.site.register(RestaurantInfo)
admin.site.register(RestaurantLocation)
admin.site.register(Special)
@admin.register(OpeningHour)
class OpeningHourAdmin(admin.ModelAdmin):
    list_display = {"day", "open_time", "close_time"}

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("description")

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('name',)