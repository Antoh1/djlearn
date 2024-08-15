from django.urls import path
from . import views


app_name = 'base'

urlpatterns = [
    path("",views.Home, name="home"),
    path("<int:list_id>/",views.Index, name="index"),
    path("status/<int:list_id>/",views.Status, name="status"),
    #path("post/",views.Post, name="posts"),
]