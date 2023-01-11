from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class StaffUser(models.Model):
    DESIGNATION = [
    ('admin', 'Admin'),
    ('writer', 'Writer'),
    ]
    user = models.OneToOneField(to=User,null=True,on_delete=models.CASCADE)
    designation=models.CharField(max_length=200,choices=DESIGNATION)

    def __str__(self) -> str:
        return self.designation