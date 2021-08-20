from django.contrib.auth.models import User
from rest_framework import serializers

from account.models import UserBasedNewsConfig


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email',]


class UserBasedNewsConfigSerializer(serializers.ModelSerializer):
    # users = UserSerializer()
    class Meta:
        model = UserBasedNewsConfig
        fields = ['id','country', 'news_sources', 'news_keywords', 'user']
