from django.urls import path
from . import views

urlpatterns = [
    path('', views.writers_home_page, name = "writers_home_page"),
    path('blogpostdetails/<str:post_id>', views.blog_post_details, name = "blog_post_details"),
    path('blogpostdetails/<str:post_id>/delete', views.delete_blog_post, name = "delete_blog_post"),
    path('blogpostdetails/<str:post_id>/postsections/add', views.add_blog_post_section, name = "add_blog_post_section"),
    path('blogpostdetails/postsections/<str:post_section_id>', views.blog_post_section_details, name = "blog_post_section_details"),
    path('blogpostdetails/postsections/<str:post_section_id>/delete', views.delete_blog_post_section, name = "delete_blog_post_section"),
]