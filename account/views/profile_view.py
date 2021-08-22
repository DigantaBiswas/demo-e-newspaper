from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework import permissions

from account.models import UserBasedNewsConfig


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        user_config = UserBasedNewsConfig.objects.filter(user_id=request.user.id).last()
        context = {
            "user_config": user_config
        }
        return render(request, "account/profile.html", context)

    def post(self, request):
        country = request.POST.get("country")
        news_keywords = request.POST.get("news_keywords")
        news_sources = request.POST.get("news_sources")
        user_config = UserBasedNewsConfig.objects.filter(user_id=request.user.id).last()
        if not user_config:
            user_config = UserBasedNewsConfig.create_user_config(request.user)
        if country:
            user_config.country = country
        if news_sources:
            user_config.news_sources = news_sources
        if news_keywords:
            user_config.news_keywords = news_keywords
        user_config.save()
        context = {
            "user_config": user_config
        }
        return render(request, "account/profile.html", context)

