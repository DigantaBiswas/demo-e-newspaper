from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, authentication, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import UserBasedNewsConfig
from newspaper.mixins import PaginationHandlerMixin
from newspaper.models import NewsArticles
from newspaper.serializers import NewsArticleSerializer


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class PersonalizedNewsFeedApiView(APIView, PaginationHandlerMixin):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    pagination_class = BasicPagination
    serializer_class = NewsArticleSerializer

    def get(self, request, format=None):
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

        page = self.paginate_queryset(news_articles)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,
                                                                           many=True).data)
        else:
            serializer = self.serializer_class(news_articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        # news_serializer = NewsArticleSerializer(news_articles, many=True)
        #
        # return Response(news_serializer.data)
