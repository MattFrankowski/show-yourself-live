from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField("get_author")

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'image', 'author', 'date_created']

    def get_author(self, obj):
        return obj.author.name
