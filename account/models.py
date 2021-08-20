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
