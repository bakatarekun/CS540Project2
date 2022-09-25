from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here. 123457890
def login(request):
    return render(request, "myapp/login.html",{})
@login_required
def index(request):
    return render(request, "myapp/index.html",{})
@login_required
def home(request):
    return render(request, "myapp/home.html",{})
