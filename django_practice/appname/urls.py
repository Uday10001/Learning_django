from django.urls import path, include
from .views import *

urlpatterns = [
    path("", tale, name="tale"),
    path("app/about", aboutTale, name='aboutTale'),
    path("app/help", hel, name="Help"),
    path("app/save_data", save_data, name = "save_data"),
    path("app/delete/<int:id>", delete_view, name = "delete_view"),
    path("app/edit/<int:id>", edit_view, name = "edit_view"),
    path("app/save_edited/<int:id>", save_edited, name = "save_edited"),
]

