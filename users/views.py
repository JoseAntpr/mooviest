from django.shortcuts import get_object_or_404,render,redirect

# Create your views here.
def index(request):
    return render(request,'users/index.html')
