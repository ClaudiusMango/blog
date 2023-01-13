from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

User=get_user_model()
# Register your models here.

admin.site.register(Blog)

class BlogSectionInlineAdmin(admin.StackedInline):
    model = BlogPostSection
    can_delete = True
    verbose_name_plural = 'Sections'

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [BlogSectionInlineAdmin]

admin.site.register(BlogPost, BlogPostAdmin)