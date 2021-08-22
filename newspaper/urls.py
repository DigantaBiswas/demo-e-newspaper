from django.urls import path

from newspaper.views.personalized_news_feed_view import PersonalizedNewsFeedView
from newspaper.views.personalized_newsfeed_api_view import PersonalizedNewsFeedApiView

#

urlpatterns = [
    path('api/personalized-news/', PersonalizedNewsFeedApiView.as_view(), name="personalized-news_api"),
    path('personalized-news/', PersonalizedNewsFeedView.as_view(), name="personalized-news"),

]
