from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("NewPage", views.NewPage,name = "NewPage"),
    path("RandomPage", views.RandomPage, name = "RandomPage"),
    path("wiki/<str:name>",views.MD_render,name = "MD")
]
