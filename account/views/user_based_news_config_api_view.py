from django.http import Http404
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import UserBasedNewsConfig
from account.serializers import UserBasedNewsConfigSerializer


class UserBasedNewsConfigApiView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """

        data = UserBasedNewsConfig.objects.all()
        user_based_news_config_serializer = UserBasedNewsConfigSerializer(data, many=True)

        return Response(user_based_news_config_serializer.data)

    def post(self, request, format=None):
        serializer = UserBasedNewsConfigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserBasedNewsConfigApiDetailView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return UserBasedNewsConfig.objects.get(pk=pk)
        except UserBasedNewsConfig.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        config = self.get_object(pk)
        serializer = UserBasedNewsConfigSerializer(config)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        config = self.get_object(pk)
        serializer = UserBasedNewsConfigSerializer(config, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
