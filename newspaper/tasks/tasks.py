from __future__ import absolute_import, unicode_literals

from datetime import datetime

from celery import shared_task
from celery import app
from django.contrib.auth.models import User
from pytz import utc

from demo_e_newspaper.celery import app
from newspaper.models import NewsArticles


@shared_task()
def schedule_populate_news_data():
    headlines = NewsArticles.news_api_fetch_top_headline_with_country_source()
    latest_news = NewsArticles.objects.filter().order_by("-published_at").last()

    articles = headlines.get("articles")
    if articles:
        for article in articles:
            source = article.get("source")
            author = article.get("author")
            title = article.get("title")
            description = article.get("description")
            url = article.get("url")
            image_url = article.get("urlToImage")
            content = article.get("content")
            published = article.get('publishedAt')
            published_datetime_object = datetime.strptime(published, '%Y-%m-%dT%H:%M:%Sz')
            published_datetime_object = utc.localize(published_datetime_object)

            if latest_news:
                if published_datetime_object > latest_news.published_at:
                    new_object = NewsArticles()
                    new_object.sources = source.get("name")
                    new_object.news_author = author
                    new_object.headline = title
                    new_object.description = description
                    new_object.news_url = url
                    new_object.image_url = image_url
                    new_object.content = content
                    new_object.published_at = published_datetime_object
                    new_object.save()
            else:
               new_object = NewsArticles()
               new_object.sources = source.get("name")
               new_object.news_author = author
               new_object.headline = title
               new_object.description = description
               new_object.news_url = url
               new_object.image_url = image_url
               new_object.content = content
               new_object.published_at = published_datetime_object
               new_object.save()