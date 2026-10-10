from rest_framework import serializers
from .models import Post

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('caption','image')

class ShowListPostsSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    is_commented = serializers.BooleanField(read_only=True)
    is_liked = serializers.BooleanField(read_only=True)

    class Meta:
        model = Post
        fields = ('id','author','caption','image','likes_count','comments_count','is_liked','is_commented','created_at','updated_at')

