from django.shortcuts import render, HttpResponse

# Create your views here. 123457890
def login(request):
    return render(request, "myapp/login.html",{})

def index(request):
    return render(request, "myapp/index.html",{})