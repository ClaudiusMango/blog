from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name = "home_page"),
    path('blogs/<str:blog_title>', views.blog, name="blog"),
    path('blogs/<str:blog_title>/<str:post_title>', views.blog_post, name="blog_post"),
]