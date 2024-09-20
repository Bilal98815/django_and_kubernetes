from django.urls import path
from . import views
from .feeds import LatestProjectsFeed


urlpatterns = [
    path("status/", view=views.status, name="status"),
    path("", view=views.home, name="home"),
    path("robots.txt", view=views.RobotsTextView.as_view(), name="robots"),
    path("rss/", view=LatestProjectsFeed(), name="rss"),
]
