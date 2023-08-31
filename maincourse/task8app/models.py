from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.login

class Article(models.Model):
    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE, null=False)
    note = models.TextField()

    def __str__(self):
        return self.note

