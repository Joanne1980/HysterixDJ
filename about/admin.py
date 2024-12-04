from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('artist', 'image', 'content', 'social_links', 'slug')
    charfield = ('artist',)
    image_field = ('images',)
    summernote_fields = ('content',)
    charfield = ('social-links',)
    prepopulated_fields = {'slug',}
    
    

