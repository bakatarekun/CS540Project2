from django.shortcuts import render

# Create your views here. 12345
def index(request):
    return render(request, "myapp/index.html",{})
