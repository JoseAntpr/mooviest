from users.models import Profile
from .serializers_users import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class AuthView(APIView):
    """
    Authentication is needed for this methods
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({'detail': "I suppose you are authenticated"})


class UserViewSet(APIView):

    def post(self,request):
        data = request.data

        if "username" not in data or "password" not in data:
            return Response(
                'Wrong credentials',
                status=status.HTTP_401_UNAUTHORIZED
            )
        user = authenticate(username=data.get('username'),password=data.get('password'))
        print(user)
        if user is None:
            return Response(
                'User non exists, please create one',
                status=status.HTTP_404_NOT_FOUND
            )
        token = Token.objects.get_or_create(user=user)

        return Response({'token':token[0].key})
