from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('username', 'content',)
    prepopulated_fields = {'username',}
    summernote_fields = ('content',)
