from rest_framework import serializers
from users.models import Profile, Collection, TypeMovie
from movie.models import Lang, Movie_lang, Movie
from django.contrib.auth.models import User
from .serializers import LangSerializer
from users.functions import register_function

class TypeMovieSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return obj.name

    def to_internal_value(self, data):
        return TypeMovie.objects.get(pk=data)

class CollectionSerializer(serializers.ModelSerializer):
    typeMovie = TypeMovieSerializer()
    class Meta:
        model = Collection
        fields = ('id', 'user','movie','typeMovie','pub_date')

class Movie_LangAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_lang
        fields = ('id','title','image')

class MoviesListSerializer(serializers.ModelSerializer):
    langs = serializers.SerializerMethodField('getMovieLang')
    class Meta:
        model = Movie
        fields = ('id', 'average', 'langs')

    def getMovieLang(self, obj):
        langs = Movie_lang.objects.get(lang = self.context['lang'], movie = obj)
        return Movie_LangAppSerializer(instance = langs).data

class ProfileRegisterSerializer(serializers.ModelSerializer):
    lang = LangSerializer()
    class Meta:
        model = Profile
        fields = ('lang','avatar',)

class UserRegisterSerializer(serializers.ModelSerializer):
    profile = ProfileRegisterSerializer()
    class Meta:
        model = User
        fields = ('id','username','email','password','profile')


    def create(self,validated_data):
        """
        Crea una instacia de User
        """
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        profile_data = validated_data.pop('profile')
        code = profile_data.get('lang').get('code')

        return register_function(username,email,password,code)

    def validate_username(self,data):
        """
        Valida si existe un usuario con este username
        """
        if User.objects.filter(username=data.lower()):
            raise serializers.ValidationError('Nombre de usuario ya registrado.')
        return data.lower()
    def validate_email(self,data):
        """
        Valida si existe un usuario con este email
        """
        if User.objects.filter(email=data.lower()):
            raise serializers.ValidationError('Ya existe un email igual en la db')
        return data.lower()

class ProfileSerializer(serializers.ModelSerializer):
    lang = LangSerializer()
    class Meta:
        model = Profile
        fields = ('born','gender','avatar','city','postalCode','lang')

class UserSerializer(serializers.ModelSerializer) :
    profile = ProfileSerializer(partial=True)
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','profile')

    def create(self,validated_data):
        print("Create")

    def update(self,instance,validated_data):
        profile_data = validated_data.pop('profile')

        profile = instance.profile

        instance.username = validated_data.get('username',instance.username)
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.email = validated_data.get('email',instance.email)

        instance.save()

        profile.born = profile_data.get('born',profile.born)
        profile.gender = profile_data.get('gender',profile.gender)
        profile.avatar = profile_data.get('avatar',profile.avatar)
        profile.city = profile_data.get('city',profile.city)
        profile.postalCode = profile_data.get('postalCode',profile.postalCode)

        profile.save()

        return instance
    def validate_username(self,data):
        user = User.objects.filter(username=data.lower())
        if self.instance is not None and self.instance.username != data and User.objects.filter(username=data.lower()):
            raise serializers.ValidationError('Nombre de usuario ya registrado.')
        else:
            return data
    def validate_email(self,data):

        if self.instance is not None and self.instance.email != data and User.objects.filter(email=data.lower()):
            raise serializers.ValidationError('Email ya registrado en la base de datos')
        else:
            return data
