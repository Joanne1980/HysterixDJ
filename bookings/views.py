from django.views.generic import TemplateView

# Create your views here.
class Playing(TemplateView):
    template_name = 'bookings/playing.html'
