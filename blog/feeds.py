from django.contrib.syndication.views import Feed
from django.utils.html import strip_tags
from django.utils.feedgenerator import Rss201rev2Feed

from .models import Post
from about.models import About


class LatestPostsFeed(Feed):
    feed_type = Rss201rev2Feed

    title = "Axror Blog"
    link = "/rss/posts/"
    description = "Latest programming posts, Django, Python, DevOps"

    def items(self):
        return Post.objects.filter(
            is_active=True
        ).order_by("-created_at")[:30]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return strip_tags(item.content)

    def item_link(self, item):
        return f"/post/{item.slug}/"

    def item_pubdate(self, item):
        return item.created_at

    def item_updateddate(self, item):
        return item.updated_at


class AboutFeed(Feed):
    feed_type = Rss201rev2Feed

    title = "About Axror"
    link = "/rss/about/"
    description = "About author and developer profile"

    def items(self):
        return About.objects.filter(
            is_active=True
        ).order_by("-created_at")[:10]

    def item_title(self, item):
        return f"{item.name} {item.surname}"

    def item_description(self, item):
        return strip_tags(item.content)

    def item_link(self, item):
        return "/about/"

    def item_pubdate(self, item):
        return item.created_at