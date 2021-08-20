# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class EditUser(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        password = request.data.get("password")

        modified = False

        existing_user = request.user

        if first_name:
            existing_user.first_name = first_name
            modified = True
        if last_name:
            existing_user.last_name = last_name
            modified = True
        if email:
            existing_user.email = email
            modified = True

        if password:
            existing_user.set_password(password)
            modified = True

        if modified:
            existing_user.save()

        return Response({'message': 'User edited '})
