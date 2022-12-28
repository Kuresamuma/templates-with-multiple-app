from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string2(request):
    return HttpResponse("<h1>This my second view of app2</h1>")
def h2(request):
    return render(request,"h2.html")