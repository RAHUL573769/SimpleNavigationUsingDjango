from . import views
from django.urls import path

urlpatterns = [
    path("contact/", views.contact),
    path("about/", views.about),
    path("home/", views.home),
]
