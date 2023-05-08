from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search/", views.search, name="search"),
    path("wiki/create/", views.createEntry, name="create"),
    path("wiki/edit/", views.editPage, name="edit"),
    path("wiki/editPage/", views.editPageRender, name="renderEdit"),
    path("wiki/random/", views.randomEntry, name="random"),
    path("wiki/<str:name>", views.loadEntry, name="wiki"),
]
