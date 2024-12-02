from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    def get_template_names(self):
        return ['home/index.html']