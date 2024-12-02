from django.views.generic import TemplateView

# Create your views here.
class Images(TemplateView):
    template_name = 'gallery/images.html'
    