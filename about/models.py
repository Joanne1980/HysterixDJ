from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class About(models.Model):
    artist = models.CharField(max_length=200,)
    featured_image = CloudinaryField('image', default='placeholder') 
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)

    


