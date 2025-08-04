from django.views.generic import TemplateView
from django.shortcuts import render


class About(TemplateView):
    template_name = 'pages/about.html'

class Rules(TemplateView):
    template_name = 'pages/rules.html'
