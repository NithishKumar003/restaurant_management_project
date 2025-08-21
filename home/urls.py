from django.urls import path
from django.contrib..auth import views as auth_views
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
    path('faq/', views.faq, name='faq'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    paath('logout/', auth_views.LogoutViews.as_view(next_page="homepage"), name="logout"),
    path('order/', views.order_page, name="order_page"),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)