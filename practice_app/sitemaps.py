from django.contrib import sitemaps
from django.urls import reverse
from .models import PracticeModel


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.7
    changefreq = "daily"

    def items(self):
        return ["status", "home", "robots"]

    def location(self, item):
        return reverse(item)


class PracticeModelSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return PracticeModel.objects.all()

    def lastmod(self, obj):
        return obj.last_modified
