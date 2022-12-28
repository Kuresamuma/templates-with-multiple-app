from django.urls import path
from app2.views import *
app2_name="something2"
urlpatterns=[
    path("string2/",string2,name="string2"),
    path("h2/",h2,name="h2"),
]