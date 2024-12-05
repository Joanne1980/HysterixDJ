from django.views.generic import TemplateView

from .models import About

# Create your views here.
class About(TemplateView):
    template_name = 'about/about.html'

