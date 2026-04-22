from django.shortcuts import render
from django.views.generic import DetailView
from .models import About

class AboutDetailView(DetailView):
    model = About
    template_name = 'about/hero.html'
    context_object_name = 'about'
    def get_object(self, queryset=None):
        return About.objects.filter(is_active=True).first()