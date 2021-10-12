from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import date, datetime
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import pre_save


class Category(models.Model):
    name = models.CharField(max_length=255)
    category_tag = models.CharField(max_length=255)
    quote = models.CharField(max_length=150, default="")
    header_img = models.CharField(max_length=255, default="")
    category_link = models.SlugField(max_length=255, unique=True, null=True)
    category_content = RichTextField(null=True, blank=True,
                                     config_name='special',
                                     external_plugin_resources=[
                                         ('youtube',
                                          '/static/ckeditor_plugins/youtube/youtube/',
                                          'plugin.js')
                                     ], )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    meta_description = models.TextField(null=False, blank=False)
    meta_keyword = models.TextField(blank=False, null=False)
    stats = models.CharField(max_length=255, default='ACTIVE')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/category/' + self.category_link + '/'


#
# class ParentCheck(models.Model):
#     sub = models.CharField(max_length=255)
# 
#     def __str__(self):
#         return self.sub


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    quote = models.CharField(max_length=150)
    header_img = models.CharField(max_length=255)
    page_link = models.SlugField(max_length=255, unique=True)
    body = RichTextField(blank=True, null=True,
                         config_name='special',
                         external_plugin_resources=[
                             ('youtube',
                              '/static/ckeditor_plugins/youtube/youtube/',
                              'plugin.js'),
                         ]
                         )
    category = models.ForeignKey(Category, default="", on_delete=models.CASCADE)
    parent_check = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    meta_description = models.TextField(null=False, blank=False)
    meta_keyword = models.TextField(blank=False, null=False)
    stats = models.CharField(default="ACTIVE", max_length=255)
    og_image = models.CharField(max_length=255, null=False, blank=False)

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/' + self.page_link + '/'


def main_slug_generator(sender, instance, *args, **kwargs):
    if not instance.page_link:
        instance.page_link = "slug"


pre_save.connect(main_slug_generator, sender=Post)


class SubPage(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    quote = models.CharField(max_length=150, default="")
    header_img = models.CharField(max_length=255, default="")
    page_link = models.SlugField(max_length=255, unique=True)
    body = RichTextField(blank=True, null=True,
                         config_name='special',
                         external_plugin_resources=[
                             ('youtube',
                              '/static/ckeditor_plugins/youtube/youtube/',
                              'plugin.js'),
                         ]
                         )
    parent_page = models.ForeignKey(Post, default="", on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    meta_description = models.TextField(null=False, blank=False)
    meta_keyword = models.TextField(blank=False, null=False)
    stats = models.CharField(default="ACTIVE", max_length=255)

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/sub/' + self.page_link + '/'


class UploadedFile(models.Model):
    file = models.FileField(upload_to='img/')

    def __str__(self):
        return self.file

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)


class IndexEditor(models.Model):
    title = models.CharField(max_length=150)
    title_tag = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    header_img = models.CharField(max_length=255)
    body_content = RichTextField(blank=True, null=True,
                                 config_name='special',
                                 external_plugin_resources=[
                                     ('youtube',
                                      '/static/ckeditor_plugins/youtube/youtube/',
                                      'plugin.js'),
                                 ]
                                 )
    meta_keyword = models.TextField()
    meta_description = models.TextField()
    copyright_content = models.TextField()

    def __str__(self):
        return self.title


class SideLinkForIndex(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DropdownURL(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DropdownTag(models.Model):
    name = models.CharField(max_length=255)
    links = models.ManyToManyField(DropdownURL)

    def __str__(self):
        return self.name
