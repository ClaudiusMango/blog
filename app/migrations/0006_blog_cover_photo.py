# Generated by Django 4.1.5 on 2023-01-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_blogpost_posted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to='blog_cover_photos'),
        ),
    ]
