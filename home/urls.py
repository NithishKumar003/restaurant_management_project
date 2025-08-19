from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='homeview'),
    path('menu/', views.homepage, name='homepage'),
    path('api/v1/menu/', views.menu_api, name='menu-api'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('reservations/', views.reservations, name='reservations'),
    path('feedback/', views.feedback_page_view, name='feedback_page'),
    path('menu/add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)