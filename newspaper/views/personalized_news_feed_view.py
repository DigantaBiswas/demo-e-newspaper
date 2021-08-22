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
                or_query = None
                for _value in config.news_sources.split(","):
                    q = Q(sources__icontains=_value)
                    if or_query is None:
                        or_query = q
                    else:
                        or_query |= q
                news_articles = news_articles.filter(or_query)

            if config.news_keywords:
                or_query = None
                for _value in config.news_keywords.split(","):

                    q = Q(headline__icontains=_value) | Q(description__icontains=_value) | Q(
                        content__icontains=_value) | Q(sources__icontains=_value)

                    if or_query is None:
                        or_query = q
                    else:
                        or_query |= q
                news_articles = news_articles.filter(or_query)

            context = {
                "news_articles": news_articles
            }
            return render(request, "newspaper/personalized_news.html", context)
