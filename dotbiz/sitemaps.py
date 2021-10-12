from django.contrib.sitemaps import Sitemap
from .views import *
from django.shortcuts import reverse


class PostSitemap(Sitemap):
    changefreq = 'always'
    priority = 1

    def items(self):
        return Post.objects.filter(stats='ACTIVE')

    def lastmod(self, obj):
        return obj.update_date


class CategorySitemap(Sitemap):
    changefreq = 'always'
    priority = 0.95

    def items(self):
        return Category.objects.filter(stats='ACTIVE')

    def lastmod(self, obj):
        return obj.update_date


class SubPageSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.9

    def items(self):
        return SubPage.objects.filter(stats='ACTIVE')

    def lastmod(self, obj):
        return obj.update_date
