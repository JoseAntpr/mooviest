import json
from django.core import serializers
from django.shortcuts import get_object_or_404
from users.models import Profile, Collection, Lang, RELATIONSHIP_FOLLOWING
from movie.models import Movie
from .serializers_users import UserRegisterSerializer, UserSerializer, CollectionSerializer, MoviesListSerializer, ProfileFollowSerializer
from .serializers import Movie_langSerializer
from .serializers_custom import MovieListCustomSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.decorators import detail_route,list_route
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from api.permissions import UserPermission
from django.forms import model_to_dict
from django.db.models import Q
from users.functions import authenticate_function

class CollectionViewSet(ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    http_method_names = ['get', 'post', 'head', 'put', 'patch']


class UserViewSet(GenericViewSet):

    #def list(self,request):
    #    return Response('listado',status=status.HTTP_200_OK)
    #queryset = User.objects.all()
    #serializer_class = UserSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (UserPermission,)

    def create(self,request):
        data = request.data
        http_code = ""
        token = None
        errors = None

        serializer = UserRegisterSerializer(data=data)

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

    def retrieve(self,request,pk):
        user = User.objects.get(pk=pk)
        profile = user.profile
        lang = Lang.objects.get(pk = profile.lang.id)

        followers = user.profile.get_followers()
        followings = user.profile.get_following()

        serializer_followers = ProfileFollowSerializer(many=True, instance=followers)
        serializer_followings = ProfileFollowSerializer(many=True, instance=followings)

        return Response(
            {
                'user':{
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'followers':serializer_followers.data,
                    'following':serializer_followings.data,
                    'profile':{
                        'born': profile.born,
                        'avatar': profile.avatar.url,
                        'city': profile.city,
                        'gender': profile.gender,
                        'postalCode': profile.postalCode,
                        'lang': {
                            'code': lang.code
                        },
                    },
                },
                'status':status.HTTP_200_OK,
            }
        )

    def update(self,request,pk=None):
        data = request.data
        http_code = ""
        errors = None

        user = get_object_or_404(User,pk=pk)
        serializer = UserSerializer(instance=user,data=data)

        if serializer.is_valid():
            user = serializer.save()
            data =  serializer.data
            http_code = status.HTTP_200_OK

        else:
            data = None
            http_code = status.HTTP_400_BAD_REQUEST
            errors = serializer.errors

        return Response(
            {
                'user': data,
                'status': http_code,
                'errors': errors
            }
        )

    #def destroy(self,request,pk):
    #    return Response('destroy',status=status.HTTP_200_OK)

    @list_route(methods = ['post'])
    def login(self,request):
        data = request.data
        message = ''
        http_code = ''
        token = None


        username = data.get('username')
        password = data.get('password')


        user = authenticate_function(username,password)


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
    @list_route(methods = ['get'])
    def search(self,request,pk=None):
        name = self.request.query_params.get('name',None)

        queryset = User.objects.filter(Q(username__icontains = name) | Q(email__icontains = name) | Q(first_name__icontains = name)).order_by('username').distinct()
        page = self.paginate_queryset(queryset)
        serializer = UserSerializer(many=True, instance=page)

        return self.get_paginated_response(serializer.data)

    @detail_route(methods = ['get'])
    def collection(self,request,pk=None):
        user = User.objects.get(pk=pk)

        name = self.request.query_params.get('name', None)
        queryset = user.profile.get_list(name)

        page = self.paginate_queryset(queryset)
        serializer = MovieListCustomSerializer(many=True, instance=page, context={'user_id': pk})

        return self.get_paginated_response(serializer.data)
    @detail_route(methods = ['get'])
    def swipelist(self,request,pk=None):
        user = User.objects.get(pk=pk)

        queryset = user.profile.get_swipe()

        page = self.paginate_queryset(queryset)
        serializer = MovieListCustomSerializer(many=True, instance=page, context={'user_id': pk})

        return self.get_paginated_response(serializer.data)

    @detail_route(methods = ['post'])
    def follow(self,request,pk=None):
        user = User.objects.get(pk=pk)
        user_id = int(request.data.get('user'))
        userFollowed = User.objects.get(pk=user_id)
        is_follow = request.data.get('is_follow')
        if is_follow:
            user.profile.follow(userFollowed.profile,RELATIONSHIP_FOLLOWING)
        else:
            user.profile.unfollow(userFollowed.profile,RELATIONSHIP_FOLLOWING)

        followings = user.profile.get_following()
        serializer_followings = ProfileFollowSerializer(many=True, instance=followings)
        return Response(
            {
                'following':serializer_followings.data,
                'status':status.HTTP_200_OK,
            }
        )
