from django.urls import path
from .views import *


urlpatterns = [
    path('', APIPreview, name='api-preview'),
    path('post-list/', PostListView, name='post-list'),
    path('post-detail/<slug:page_link>/', post_detail_view, name='post-detail'),
    path('sub-post-list/', sub_post_list, name='sub-post-list'),
    path('sub-post-detail/<slug:page_link>/', sub_post_detail, name='sub-post-detail'),
    path('category-list/', category_list, name='category-list'),
    path('category-detail/<slug:category_link>/', category_detail, name='category-detail')
]
