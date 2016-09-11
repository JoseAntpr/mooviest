from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type':'password'}
    )

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
    profile = ProfileSerializer(partial=True)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','profile')

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
        if self.instance is not None and self.instance.username != data and user = User.objects.filter(username=data.lower()):
            raise serializers.ValidationError('Nombre de usuario ya registrado.')
        else:
            return data
    def validate_email(self,data):

        if self.instance is not None and self.instance.email != data and User.objects.filter(email=data.lower()):
            raise serializers.ValidationError('Email ya registrado en la base de datos')
        else:
            return data
