from django.db.models import Q
from django.shortcuts import render
from django.views import View

from account.models import UserBasedNewsConfig
from newspaper.models import NewsArticles


class PersonalizedNewsFeedView(View):
    def get(self, request):
        config = UserBasedNewsConfig.objects.filter(user_id=request.user.id).last()
        news_articles = NewsArticles.objects.all()
        if config:
            if config.news_sources:
                news_articles = news_articles.filter(sources__icontains=config.news_sources.split(","))

            if config.news_keywords:
                news_articles = news_articles.filter(Q(sources__icontains=config.news_keywords.split(",")) | Q(
                    headline__icontains=config.news_keywords.split(",")) | Q(
                    description__icontains=config.news_keywords.split(",")) | Q(
                    content__icontains=config.news_keywords.split(",")))
        context = {
            "news_articles": news_articles
        }
        return render(request, "newspaper/personalized_news.html", context)