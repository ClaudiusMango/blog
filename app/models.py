from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class Writer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    display_name = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self) -> str:
        if self.display_name != None:
            return self.display_name
        else:
            try:
                return f"{self.user.first_name } {self.user.last_name}"
            except:
                return super().__str__()
    @property
    def image_url(self):
        try:
            url = self.profile_picture.url
        except:
            url = ''

        return url

class Blog(models.Model):
    title = models.CharField(max_length=200)
    cover_photo = models.ImageField(upload_to='blog_cover_photos')

    def __str__(self) -> str:
        try:
            return self.title
        except:
            return super().__str__()
    
    @property
    def image_url(self):
        try:
            url = self.cover_photo.url
        except:
            url = ''

        return url

    @property
    def posts(self):
        return self.blogpost_set.all()


class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    post_by = models.ForeignKey(Writer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    introduction = models.TextField()
    posted_on = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        try:
            return f"{self.title} by {self.post_by} for {self.blog.title} blog"
        except:
            return super().__str__()
    
    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url

    @property
    def post_sections(self):
        return self.blogpostsection_set.all()

class BlogPostSection(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    content = models.TextField()

    def __str__(self) -> str:
        try:
            return self.sub_title
        except:
            return super().__str__()