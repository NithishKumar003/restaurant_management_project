from django.conf import settings

def restaurant_opening_hours(request):
    return {
        'opening_hours': getattr(settings, 'RESTAURANT_OPENING_HOURS', 'Hours not available')
    }
