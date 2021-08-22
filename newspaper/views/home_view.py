from django.db.models import Q
from django.shortcuts import render
from django.views import View

from account.models import UserBasedNewsConfig
from newspaper.models import NewsArticles


class HomeView(View):
    def get(self, request):

        news_articles = NewsArticles.objects.all()

        context = {
            "news_articles": news_articles
        }
        return render(request, "newspaper/personalized_news.html", context)