from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here. 123457890
def login(request):
    return render(request, "myapp/login.html",{})
@login_required
def index(request):
    data = User.objects.raw("SELECT * FROM auth_user;")
    return render(request, "myapp/index.html",{'data' : data})
@login_required
def home(request):
    return render(request, "myapp/home.html",{})
