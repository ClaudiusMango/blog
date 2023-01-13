from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  get_user_model

from accounts.models import StaffUser
from app.models import BlogPost, BlogPostSection
from writers.forms import BlogPostForm, BlogPostSectionForm
from datetime import datetime
from django.shortcuts import redirect
User=get_user_model()


@login_required(login_url='/accounts/signin/')
def writers_home_page(request):
    user = User.objects.get(username=request.user.username)
    staff_user,created = StaffUser.objects.get_or_create(user=user)
    posts = staff_user.blogpost_set.all()
    if request.method == 'POST':
        filled_form = BlogPostForm(request.POST, request.FILES)
        if filled_form.is_valid():

            new_post = BlogPost.objects.create(
                blog = filled_form.cleaned_data['blog'],
                title = filled_form.cleaned_data['title'],
                image = filled_form.cleaned_data['image'],
                introduction = filled_form.cleaned_data['introduction'],
                post_by=staff_user,
                posted_on = datetime.today()
            )
            return redirect('blog_post_details', new_post.id)

        else:
            context = {
                'posts': posts,
                'add_post_form': filled_form,
            }
            return render(request, 'writers/writers_home_page.html',context)
    else:
        context = {
            'posts': posts,
            'add_post_form': BlogPostForm(),
        }
        return render(request, 'writers/writers_home_page.html',context)

@login_required(login_url='/accounts/signin/')
def blog_post_details(request,post_id):
    user = User.objects.get(username=request.user.username)
    staff_user,created = StaffUser.objects.get_or_create(user=user)
    posts = staff_user.blogpost_set.all()
    post = BlogPost.objects.get(id=post_id)
    if request.method == 'POST':
        filled_form = BlogPostForm(request.POST, request.FILES, initial={
                    'blog':post.blog,
                    'title':post.title,
                    'image':post.image,
                    'introduction':post.introduction,
                },instance=post)
        if filled_form.has_changed():
            if filled_form.is_valid():
                filled_form.save()
                return redirect('blog_post_details', post.id)
            else:
                context = {
                    'post':post,
                    'posts': posts,
                    'blog_post_details_form': filled_form,
                    'show_post_details_modal':True
                }
                return render(request, 'writers/writers_home_page.html',context)
        else:
            filled_form.add_error(field=None,error='No change was detected')
            context = {
                    'post':post,
                    'posts': posts,
                    'blog_post_details_form': filled_form,
                    'show_post_details_modal':True
                }
            return render(request, 'writers/writers_home_page.html',context)
    else:
        context = {
            'post':post,
            'posts': posts,
            'blog_post_details_form': BlogPostForm(
                initial={
                    'blog':post.blog,
                    'title':post.title,
                    'image':post.image,
                    'introduction':post.introduction,
                }
            ),
            'show_post_details_modal':True
        }
    return render(request, 'writers/writers_home_page.html',context)

@login_required(login_url='/accounts/signin/')
def delete_blog_post(request,post_id):
    post = BlogPost.objects.get(id=post_id)
    post.delete()
    return redirect('writers_home_page')


@login_required(login_url='/accounts/signin/')
def add_blog_post_section(request,post_id):
    user = User.objects.get(username=request.user.username)
    staff_user,created = StaffUser.objects.get_or_create(user=user)
    posts = staff_user.blogpost_set.all()
    post = BlogPost.objects.get(id=post_id)

    if request.method == 'POST':
        filled_form = BlogPostSectionForm(
            request.POST,
            request.FILES
        )

        if filled_form.is_valid():
            BlogPostSection.objects.create(
                blog_post = post,
                sub_title = filled_form.cleaned_data['sub_title'],
                image = filled_form.cleaned_data['image'],
                content = filled_form.cleaned_data['content'],
            )
            return redirect('blog_post_details', post.id)
        else:
            context ={
                'post':post,
                'posts': posts,
                'add_blog_post_section_form': filled_form,
                'show_add_post_section_modal':True
            }
            return render(request, 'writers/writers_home_page.html',context)
    else:
        context = {
            'post':post,
            'posts': posts,
            'add_blog_post_section_form': BlogPostSectionForm(),
            'show_add_post_section_modal':True
        }
    return render(request, 'writers/writers_home_page.html',context)

@login_required(login_url='/accounts/signin/')
def blog_post_section_details(request,post_section_id):
    user = User.objects.get(username=request.user.username)
    staff_user,created = StaffUser.objects.get_or_create(user=user)
    posts = staff_user.blogpost_set.all()
    post_section = BlogPostSection.objects.get(id=post_section_id)

    if request.method == 'POST':
        filled_form = BlogPostSectionForm(
                request.POST,
                request.FILES,
                initial={
                    'blog_post':post_section.blog_post,
                    'sub_title':post_section.sub_title,
                    'image':post_section.image,
                    'content':post_section.content,
                },
                instance=post_section
            )
        if filled_form.has_changed():
            if filled_form.is_valid():
                filled_form.save()
                return redirect('blog_post_section_details', post_section.id)
            else:
                context = {
                    'post_section':post_section,
                    'posts': posts,
                    'blog_post_section_details_form': filled_form,
                    'show_post_section_details_modal':True
                }
                return render(request, 'writers/writers_home_page.html',context)
        else:
            filled_form.add_error(field=None,error='No change was detected')
            context = {
                    'post_section':post_section,
                    'posts': posts,
                    'blog_post_section_details_form': filled_form,
                    'show_post_section_details_modal':True
                }
            return render(request, 'writers/writers_home_page.html',context)
    else:
        context = {
            'post_section':post_section,
            'posts': posts,
            'blog_post_section_details_form': BlogPostSectionForm(
                initial={
                    'blog_post':post_section.blog_post,
                    'sub_title':post_section.sub_title,
                    'image':post_section.image,
                    'content':post_section.content,
                }
            ),
            'show_post_section_details_modal':True
        }
    return render(request, 'writers/writers_home_page.html',context)

@login_required(login_url='/accounts/signin/')
def delete_blog_post_section(request,post_section_id):
    post_section = BlogPostSection.objects.get(id=post_section_id)
    post_section.delete()
    return redirect('blog_post_details', post_section.blog_post.id)