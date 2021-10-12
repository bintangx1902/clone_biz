from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from dotbiz.sitemaps import *
from django.views.generic import TemplateView

handler404 = 'dotbiz.views.handler404'
handler500 = 'dotbiz.views.handler500'
handler400 = 'dotbiz.views.handler400'
handler403 = 'dotbiz.views.handler403'

sitemaps = {
    'posts': PostSitemap,
    'category': CategorySitemap,
    'subpage': SubPageSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('download/<path>', serve, settings.MEDIA_ROOT),
    path('static/<path>', serve, settings.STATIC_ROOT),
    path('media/<path>', serve, settings.MEDIA_ROOT),
    path('robots.txt', include('robots.urls')),

]

if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [path('', include('dotbiz.urls')), ]

