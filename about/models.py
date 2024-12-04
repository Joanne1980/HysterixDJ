from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class About(models.Model):
    artist = models.CharField(max_length=200,)
    image = models.ImageField() 
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)