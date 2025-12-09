from rest_framework import serializers
from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "author", "content", "created_at", "likes_count"]
