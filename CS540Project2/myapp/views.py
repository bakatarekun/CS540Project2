from django.shortcuts import render

# Create your views here. 123457890
def login(request):
    return render(request, "myapp/login.html",{})
