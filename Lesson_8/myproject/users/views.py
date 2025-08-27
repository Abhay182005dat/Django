from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # django already provides us various things for registering  etc

# Create your views here.
def register_view(request):
    form = UserCreationForm()
    return render(request,"users/register.html", {"form":form})