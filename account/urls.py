from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
#
from account.views import LogoutView
from account.views.custom_user_api_view import CustomUserApiView, CustomUserApiDetailView
from account.views.edit_user_api_view import EditUser
from account.views.login_view import LoginView
from rest_framework import routers

from account.views.logout_api_view import LogoutApiView
from account.views.user_based_news_config_api_view import UserBasedNewsConfigApiView, UserBasedNewsConfigApiDetailView
from account.views.user_registration_view import UserRegistrationView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign-up/', UserRegistrationView.as_view(), name='signup'),
    # path('api/login-token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', CustomUserApiView.as_view(), name='user'),
    path('api/user/<pk>/', CustomUserApiDetailView.as_view(), name='user_detail'),
    # path('api/edit-user/', EditUser.as_view(), name='edit_user'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/user-settings/', UserBasedNewsConfigApiView.as_view(), name="user_settings"),
    path('api/user-settings/<pk>/', UserBasedNewsConfigApiDetailView.as_view(), name="user_settings_detail"),
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/logout/', LogoutApiView.as_view()),
]
