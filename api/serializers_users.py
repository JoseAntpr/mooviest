from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.models import User

class ProfileRegisterSerializer(serializers.Serializer):
    born = serializers.DateField()

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type':'password'}
    )
    profile = ProfileRegisterSerializer()

    def create(self,validated_data):
        """
        Crea una instacia de User
        """
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        profile = validated_data.get('profile')


        user = User.objects.create_user(username=username,password=password,email=email)
        user_profile = Profile()
        user_profile.user = user
        user_profile.born = profile['born']
        user_profile.save()

        return user


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
    class Meta:
        model = Profile
        fields = ('born','gender','avatar','city','postalCode')

class UserSerializer(serializers.ModelSerializer) :
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','profile')
