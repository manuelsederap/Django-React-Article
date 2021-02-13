from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.Serializer):
    """Convert/Serialize Article queryset into JSON datatype"""

    class Meta:
        model = Article
        fields = ['id', 'title', 'description']
