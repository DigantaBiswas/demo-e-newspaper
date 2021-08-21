from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import UserSerializer


class CustomUserApiView(APIView):
    """
        View to list all users in the system.

        * Requires token authentication.
        * Only admin users are able to access this view.
        """

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """

        data = User.objects.all()
        user_serializer = UserSerializer(data, many=True)

        return Response(user_serializer.data)

    def post(self, request, format=None):
        email = request.data.get("email")
        user_name = request.data.get("username")
        password = request.data.get("password")

        if all([user_name, password]):
            new_obj = User()
            new_obj.username = user_name
            new_obj.set_password(password)
            if email:
                new_obj.email = email
            new_obj.save()

            user_serializer = UserSerializer(new_obj, many=False)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(UserSerializer._errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserApiDetailView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        config = self.get_object(pk)
        serializer = UserSerializer(config)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        email = request.data.get("email")
        user_name = request.data.get("username")
        password = request.data.get("password")

        if all([user_name, password]):
            user.username = user_name
            user.set_password(password)
            if email:
                user.email = email
            user.save()

            user_serializer = UserSerializer(user, many=False)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(UserSerializer._errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
