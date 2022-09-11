from django.shortcuts import render

# Create your views here. 12345ABC
def index(request):
    return render(request, "myapp/index.html",{})
