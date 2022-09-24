from django.shortcuts import render

# Create your views here. 123457890
def index(request):
    return render(request, "myapp/index.html",{})
