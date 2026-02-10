from django.urls import path, include
from .views import *

urlpatterns = [
    path("", tale, name="tale"),
    path("about", aboutTale, name='aboutTale'),
    path("help", hel, name="Help"),
    path("save_data", save_data, name = "save_data")
]

