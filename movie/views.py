
from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'home.html',{'name':'Sebastian Arias'})

def about(request):
    return render (request, 'about.html')