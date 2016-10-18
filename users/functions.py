from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def authenticate_function(username, password):
    if '@' in username:
        try:
            username = User.objects.get(email=username)
        except User.DoesNotExist:
            username = None

    return authenticate(username=username, password=password)
