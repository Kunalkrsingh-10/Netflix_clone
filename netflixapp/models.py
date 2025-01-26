from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Constants
AGE_LIMITS = ( 
    ('All', 'All'),
    ('Kids', 'Kids')
)
MOVIE_CHOICE = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single')
)

# Models
class CustomUser(AbstractUser):
    profile = models.ManyToManyField('Profile', blank=True, related_name='customers')

class Profile(models.Model):    
    name = models.CharField(max_length=255, null=True)
    age_limit = models.CharField(choices=AGE_LIMITS, max_length=50)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.name or "Unnamed Profile"

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    type = models.CharField(choices=MOVIE_CHOICE, max_length=50)
    video = models.ManyToManyField('Video', related_name='movies')  # Or ForeignKey if 1:1
    image = models.ImageField(upload_to='covers')
    age_limit = models.CharField(choices=AGE_LIMITS, max_length=50)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='movies')

    def __str__(self):
        return self.title
