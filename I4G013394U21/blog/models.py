from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    def __str__(self):
        return self.Title