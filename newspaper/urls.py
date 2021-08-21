from django.urls import path

from newspaper.views.personalized_newsfeed_view import PersonalizedNewsFeedApiView

#

urlpatterns = [
    path('api/personalized-news/', PersonalizedNewsFeedApiView.as_view(), name="personalized-news"),

]
