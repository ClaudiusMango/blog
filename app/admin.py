from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

User=get_user_model()
# Register your models here.

admin.site.register(Blog)

class WriterInlineAdmin(admin.StackedInline):
    model = Writer
    can_delete = True
    verbose_name_plural = 'Writers'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
        'fields': ('is_active', 'is_staff', 'is_superuser'),
    }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),)
    inlines = [WriterInlineAdmin]

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

class BlogSectionInlineAdmin(admin.StackedInline):
    model = BlogPostSection
    can_delete = True
    verbose_name_plural = 'Sections'

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [BlogSectionInlineAdmin]

admin.site.register(BlogPost, BlogPostAdmin)