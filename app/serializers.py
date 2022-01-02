from rest_framework import serializers
from .models import Post, Result

class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Post
        fields = ('id', 'title', 'image', 'content', 'created_at')

class ResultSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Result
        fields = ('id', 'title', 'image', 'content', 'skill', 'created_at')