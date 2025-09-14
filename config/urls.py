from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve as static_serve
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from main.sitemaps import StaticViewSitemap
from main import views

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [

    path("admin/", admin.site.urls),

    path("", include("main.urls")),

    path("robots.txt", views.robots_txt, name="robots"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),

    path("favicon.ico", RedirectView.as_view(
        url="/static/img/favicon.ico", permanent=True)),
]

if settings.DEBUG:re_path(
        r"^\.well-known/appspecific/(?P<path>.+)$",
        static_serve,
        {"document_root": settings.BASE_DIR / "well_known" / "appspecific"},
        name="well_known_appspecific",
    ),

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)