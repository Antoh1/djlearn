from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home, name="home"),
    path("<int:item_id>/",views.Index, name="index"),
    #path("post/",views.Post, name="posts"),
]