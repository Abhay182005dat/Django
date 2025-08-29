from django.db import models
from django.contrib.auth.models import User  # For user authentication and relationships

# Create your models here.
class post(models.Model):
    # Core post fields
    title = models.CharField(max_length=75)  # Title with max 75 characters
    body = models.TextField()                # Main content without length limit
    slug = models.SlugField()               # URL-friendly version of title
    date = models.DateTimeField(auto_now_add=True) # everytime user adds a post data and time is added
    
    # Media and relationships
    banner = models.ImageField(default='fallback.png', blank=True)  # Optional post image
    author = models.ForeignKey(User, on_delete=models.CASCADE , default=None)      # Links to User model, CASCADE deletes posts when user is deleted

# Above line was till Lesson_3

    def __str__(self):
        return self.title     # Migrations is not necessary here beacuse we are not playing with data , its just