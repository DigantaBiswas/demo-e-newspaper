from rest_framework import serializers

from newspaper.models import NewsArticles


class NewsArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsArticles
        fields = ["id", "headline", "sources", "news_url", "image_url"]
