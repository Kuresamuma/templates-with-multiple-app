from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string1(request):
    return HttpResponse("<h1>This is my first app1 of view</h1>")

def h1(request):
    return render(request,"h1.html")