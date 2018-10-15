from django.shortcuts import render
from django.views.generic import TemplateView

class SettingsViewView(TemplateView):
    template_name = "view_settings.html"