from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dotbiz.models import Post, SubPage, Category
from .serializers import PostSerializer, SubPageSerializer, CategorySerializer


@api_view(['GET'])
def APIPreview(request):
    api_urls = {
        'Post': '/<slug:page_link>/',
        'Sub Post': '/sub/<slug:page_link>/',
        'Category': '/category/<slug:category_link>/',
        'Search Result': '/search/Q',
        'Older Post': '/post/older/'
    }

    return Response(api_urls)


@api_view(['GET'])
def PostListView(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_detail_view(request, page_link):
    post = Post.objects.get(page_link=page_link)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def sub_post_list(request):
    sub = SubPage.objects.all()
    serializer = SubPageSerializer(sub, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sub_post_detail(req, page_link):
    sub = SubPage.objects.get(page_link=page_link)
    serializer = SubPageSerializer(sub, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def category_list(request):
    cate = Category.objects.all()
    serializer = CategorySerializer(cate, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_detail(req, category_link):
    cate = Category.objects.get(category_link=category_link)
    serializer = CategorySerializer(cate, many=False)
    return Response(serializer.data)
