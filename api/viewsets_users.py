from users.models import Profile,Collection
from .serializers_users import UserRegisterSerializer,UserSerializer,CollectionSerializer
from .serializers import Movie_langSerializer
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

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


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
            data = None
            message = 'User or password incorrect'
            http_code = status.HTTP_404_NOT_FOUND
        else:
            message = 'Login successfully'
            http_code = status.HTTP_200_OK
            token = Token.objects.get_or_create(user=user)[0].key
            data = {
                'id':user.id,
                'username':user.username,
                'email':user.email,
                'profile': {
                    'lang': {
                        'code': user.profile.lang.code,
                    },
                    'avatar': str(user.profile.avatar)
                }
            }

        return Response(
            {
                'message': message,
                'user': data,
                'status': http_code,
                'token': token,
            }
        )
    @detail_route(methods = ['get'])
    def seen_list(self,request,pk=None):

        user = User.objects.get(pk=pk)
        queryset = user.profile.get_seenlist()
        serializer = Movie_langSerializer(queryset,many=True)

        return Response(serializer.data)
    @detail_route(methods = ['get'])
    def watchlist(self,request,pk=None):
        print(request.data)
        user = User.objects.get(pk=pk)
        queryset = user.profile.get_watchlist()
        serializer = Movie_langSerializer(queryset,many=True)

        return Response(serializer.data)
    @detail_route(methods = ['get'])
    def swipe_list(self,request,pk=None):
        print(request.data)
        user = User.objects.get(pk=pk)
        queryset = user.profile.get_swipelist()
        serializer = Movie_langSerializer(queryset,many=True)

        return Response(serializer.data)
    @detail_route(methods = ['get'])
    def favourite_list(self,request,pk=None):
        print(request.data)
        user = User.objects.get(pk=pk)
        queryset = user.profile.get_favouritelist()
        serializer = Movie_langSerializer(queryset,many=True)

        return Response(serializer.data)
