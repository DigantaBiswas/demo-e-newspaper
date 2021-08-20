from django.urls import path
from rest_framework_simplejwt import views as jwt_views
#
from account.views import LogoutView
from account.views.custom_user_api_view import CustomUser
from account.views.edit_user_api_view import EditUser
from account.views.login_view import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/login-token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/create-user/', CustomUser.as_view(), name='create_user'),
    # path('api/edit-user/', EditUser.as_view(), name='edit_user'),
]
