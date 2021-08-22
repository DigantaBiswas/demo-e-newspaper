from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from base.models import BaseAbstractModel


class UserBasedNewsConfig(BaseAbstractModel):
    country = models.CharField(max_length=255, blank=True, null=True)
    news_sources = models.CharField(max_length=255, blank=True, null=True)
    news_keywords = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, related_name='user_based_config', on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = "account"

    @classmethod
    def create_user_config(cls, user, country=None, news_sources=None, news_keywords=None):
        if not cls.objects.filter(user_id=user.id):
            new_obj = cls()
            new_obj.user = user
            if country:
                new_obj.country = country
            if news_keywords:
                new_obj.news_keywords = news_keywords
            if news_sources:
                new_obj.news_sources = news_sources
            new_obj.save()
