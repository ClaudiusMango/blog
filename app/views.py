from django.shortcuts import render
import urllib.parse
from app.models import Blog,BlogPost


def home_page(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request, 'app/home.html', context)

def blog(request,blog_title):
    title = urllib.parse.unquote_plus(blog_title)
    blog = Blog.objects.get(title=title)
    context = {
        'blog':blog
    }
    return render(request, 'app/blog.html', context)

def blog_post(request,blog_title,post_title):
    title = urllib.parse.unquote_plus(post_title)
    post = BlogPost.objects.get(title=title)
    context = {
        'post':post
    }
    return render(request, 'app/blog_post.html', context)
