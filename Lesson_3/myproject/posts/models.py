from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True) # everytime user adds a post data and time is added
