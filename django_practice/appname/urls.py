from django.urls import path, include
from .views import *

urlpatterns = [
    path("", tale, name="tale"),
    path("about", aboutTale, name='aboutTale'),
    path("help", hel, name="Help")

]

