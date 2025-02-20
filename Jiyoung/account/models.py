from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    company_name = models.CharField(max_length=50)
    company_logo = models.ImageField(upload_to = "account/", blank = True, null=True)

    def __str__(self):
        return self.username