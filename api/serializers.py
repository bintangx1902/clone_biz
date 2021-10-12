from rest_framework import serializers
from dotbiz.models import Post, SubPage, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class SubPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPage
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
