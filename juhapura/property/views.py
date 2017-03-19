from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class PropertyHomePageView(TemplateView):
    # model = User
    # # These next two lines tell the view to index lookups by username
    # slug_field = 'username'
    # slug_url_kwarg = 'username'    
    template_name = 'property/index.html'