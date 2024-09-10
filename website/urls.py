from django.urls import path
from .views import *


urlpatterns = [
  path('', home, name="home"),
  path('gallery/', gallery, name='gallery'),
  path('contact/', contact, name="contact"),
  path('about/', about, name="about"),
  path('promo/', promo, name='promo'),
  path('stock/', stock, name='stock'),
  path('events/', events, name='events'),
]
