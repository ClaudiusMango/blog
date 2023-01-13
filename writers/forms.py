from django import forms
from app.models import BlogPost, BlogPostSection
from ckeditor.widgets import CKEditorWidget
from tinymce.widgets import TinyMCE


# class BlogPostForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = BlogPostSection
#         # exclude = ['post_by','posted_on']
#         fields = '__all__'



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['post_by','posted_on']

class BlogPostSectionForm(forms.ModelForm):
    class Meta:
        model = BlogPostSection
        exclude = ['blog_post']