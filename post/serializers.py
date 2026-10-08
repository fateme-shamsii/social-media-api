from rest_framework import serializers
from .models import Post

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('caption','image')

class ShowListPostsSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Post
        fields = ('id','author','caption','image','created_at','updated_at')

