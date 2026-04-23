from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post
from about.models import About


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = Post.objects.filter(is_active=True).count()
        context['latest_posts'] = Post.objects.filter(is_active=True).order_by('-created_at')[:7]
        context['about_short'] = About.objects.filter(is_active=True).first()
        return context