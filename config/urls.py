from django.contrib import admin
from django.urls import path , include
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import PostSitemap, AboutSitemap , AchievementSitemap
from blog.feeds import LatestPostsFeed, AboutFeed
sitemaps = {
    "posts": PostSitemap,
    "about": AboutSitemap,
    "achievements": AchievementSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor5/',include('django_ckeditor_5.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('', include('asosiy.urls')),
    path("sitemap.xml",sitemap,{"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap"),
    path("rss/posts/",LatestPostsFeed(),name="posts_rss"),
    path("rss/about/",AboutFeed(),name="about_rss"),
    path('accounts/', include('allauth.urls')),
]
handler404 = 'asosiy.views.custom_page_not_found'