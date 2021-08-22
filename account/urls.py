from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

#
from account.views import LogoutView
from account.views.custom_user_api_view import CustomUserApiView, CustomUserApiDetailView
from account.views.login_view import LoginView
from account.views.logout_api_view import LogoutApiView
from account.views.profile_view import ProfileView
from account.views.user_based_news_config_api_view import UserBasedNewsConfigApiView, UserBasedNewsConfigApiDetailView
from account.views.user_registration_view import UserRegistrationView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign-up/', UserRegistrationView.as_view(), name='signup'),
    path('api/user/', CustomUserApiView.as_view(), name='user'),
    path('api/user/<pk>/', CustomUserApiDetailView.as_view(), name='user_detail'),
    path('api/user-settings/', UserBasedNewsConfigApiView.as_view(), name="user_settings"),
    path('api/user-settings/<pk>/', UserBasedNewsConfigApiDetailView.as_view(), name="user_settings_detail"),
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/logout/', LogoutApiView.as_view()),
    path('profile/', ProfileView.as_view(), name="user_profile"),
]
