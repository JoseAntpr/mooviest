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
        data = request.data
        http_code = ""
        token = None
        errors = None

        serializer = UserRegisterSerializer(data=data)
        print (serializer)
        if serializer.is_valid():
            user = serializer.save()
            data =  serializer.data
            http_code = status.HTTP_201_CREATED
            token = Token.objects.get_or_create(user=user)[0].key

        else:
            data = None
            http_code = status.HTTP_400_BAD_REQUEST
            errors = serializer.errors

        return Response(
            {
                'user':data,
                'status':http_code,
                'token':token,
                'errors':errors
            }
        )

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


        username = data.get('username')
        if '@' in username:
            print (username)
            user_aux = User.objects.filter(email=username)[0]
            user = authenticate(username=user_aux.username,password=data.get('password'))
        else:
            user = authenticate(username=data.get('username'),password=data.get('password'))

        if user is None:
            message = 'User or password incorrect'
            http_code = status.HTTP_404_NOT_FOUND
        else:
            message = 'Login successfully'
            http_code = status.HTTP_200_OK
            token = Token.objects.get_or_create(user=user)[0].key

        return Response(
            {
                'message': message,
                'status': http_code,
                'token': token,
            }
        )
