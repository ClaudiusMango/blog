# Generated by Django 4.1.5 on 2023-01-10 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_blogsection_blogpostsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='posted_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]
