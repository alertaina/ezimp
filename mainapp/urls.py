from django.urls import path
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from . import views
from .models import *


app_name = 'mainapp'

urlpatterns = [
    # Inicio
    path('index', TemplateView.as_view(template_name = 'mainapp/index.html'), name='index'),
    path('', TemplateView.as_view(template_name = 'mainapp/index.html')),
]