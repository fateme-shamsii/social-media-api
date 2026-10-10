from rest_framework import serializers

from .models import Comment

class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text',)


class ShowCommentForAllPostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created_at', 'updated_at')


class EditCommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    post = serializers.CharField(source='post.caption', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text')
        read_only_fields = ('id', 'author', 'post')