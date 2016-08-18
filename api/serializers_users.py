from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('born','gender','city')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only = True)
    class Meta:
        model = User
        fields = ('username','profile')
