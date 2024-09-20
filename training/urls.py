from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from practice_app.sitemaps import StaticViewSitemap, PracticeModelSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "models": PracticeModelSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('practice_app.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
