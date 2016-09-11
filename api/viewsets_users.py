from users.models import Profile
from .serializers_users import UserRegisterSerializer,UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.decorators import detail_route,list_route
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.viewsets import ViewSet,ModelViewSet


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(ModelViewSet):

    #def list(self,request):
    #    return Response('listado',status=status.HTTP_200_OK)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self,request):
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)
            return Response({'user':serializer.data,'status':status.HTTP_201_CREATED,'token':token[0].key})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #def retrieve(self,request,pk):
    #    return Response('retrieve',status=status.HTTP_200_OK)
    #def update(self,request,pk):
    #    return Response('update',status=status.HTTP_200_OK)
    #def destroy(self,request,pk):
    #    return Response('destroy',status=status.HTTP_200_OK)

    @list_route(methods = ['post'])
    def login(self,request):
        data = request.data
        message = ''
        http_code = ''
        token = None

        if "username" not in data or "password" not in data:
            message = 'Wrong credentials'
            http_code = status.HTTP_401_UNAUTHORIZED
        else:
            user = authenticate(username=data.get('username'),password=data.get('password'))
            if user is None:
                message = 'User non exists, please create one'
                http_code = status.HTTP_404_NOT_FOUND
            else:
                message = 'Login successfully'
                http_code = status.HTTP_200_OK
                token = Token.objects.get_or_create(user=user)[0].key

        return Response(
            {
                'message': message,
                'status': http_code,
                'token': token
            }
