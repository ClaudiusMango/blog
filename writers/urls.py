from django.urls import path
from . import views

urlpatterns = [
    path('', views.writers_home_page, name = "writers_home_page"),
]