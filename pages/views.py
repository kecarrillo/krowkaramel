# pages/views.py
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'homepage.html'
