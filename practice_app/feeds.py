from django.contrib.syndication.views import Feed
from .models import PracticeModel


class LatestProjectsFeed(Feed):
    title = "My Projects"
    link = "/rss/"
    description = "Updates on the latest posts from my projects."

    def items(self):
        return PracticeModel.objects.order_by('-created_at')[:5]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return item.slug
