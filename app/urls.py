from django.urls import path
from .views import *


urlpatterns = [
  path('login', loginView, name="login"),
  path('logout', logout, name="logout"),


]
