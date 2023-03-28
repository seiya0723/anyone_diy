from django.urls import path
from . import views

app_name    = "diy"
urlpatterns = [ 
    path("", views.index, name="index"),
]




