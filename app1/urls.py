from django.urls import path
from app1.views import*
app1_name="something1"
urlpatterns=[
    path("string1/",string1,name="string1"),
    path("h1/",h1,name="h1"),
]