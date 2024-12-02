from django.views.generic import TemplateView

# Create your views here.
class Music(TemplateView):
    template_name = 'music/music.html'