from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post
from about.models import About, Achievement


class PostSitemap(Sitemap):
    protocol = "https"
    changefreq = "daily"
    priority = 0.9
    limit = 5000

    def items(self):
        return Post.objects.filter(is_active=True)

    @staticmethod
    def lastmod( obj):
        return obj.updated_at


    def location(self, obj):
        return f"/post/{obj.slug}/"


class AboutSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return About.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse("about")

class AchievementSitemap(Sitemap):
    protocol = "https"
    changefreq = "daily"
    priority = 0.9
    limit = 5000
    def items(self):
        return Achievement.objects.filter(is_active=True)
    def lastmod(self, obj):
        return obj.created_at
    def location(self, obj):
        return f"/achievement/{obj.id}/"

