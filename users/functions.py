from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import Profile
from movie.models import Lang

def authenticate_function(username, password):
    if '@' in username:
        try:
            username = User.objects.get(email=username)
        except User.DoesNotExist:
            username = None

    return authenticate(username=username, password=password)

def register_function(username,email,password,lang):
    user_model = User.objects.create_user(username=username,password=password,email=email)

    user_profile = Profile()
    user_profile.user = user_model
    user_profile.lang = Lang.objects.get(code=lang)

    user_profile.save()

    return authenticate(username=username, password=password)
