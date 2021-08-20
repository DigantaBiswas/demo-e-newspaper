from django.db import models

# Create your models here.
from newsapi import NewsApiClient

from base.models import BaseAbstractModel


class NewsArticles(BaseAbstractModel):
    sources = models.JSONField(blank=True)
    news_author = models.CharField(max_length=255, blank=True, null=True)
    headline = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    news_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True,null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        app_label = "newspaper"


    def news_api_fetch_with_country_source(self, country="us", sources="bbc-news,the-verge", q=None):
        newsapi = NewsApiClient(api_key='158c339162d945d38f981a53096b103e')

        # /v2/top-headlines
        top_headlines = newsapi.get_top_headlines(q=q,
                                                  sources=sources,
                                                  # category='business',
                                                  language='en',
                                                  country=country)
        return top_headlines
