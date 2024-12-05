from django.views.generic import TemplateView

# Create your views here.
class Tunes(TemplateView):
    template_name = 'music/tunes.html'