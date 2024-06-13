from django.urls import path

from . import views

urlpatterns = [
    path("",views.indexfunction,name="index"),
    path("connv", views.conNavFunction,name = "connav"),
    path("back", views.backFunction,name = "back"),
    path("contact",views.contactFunction,name="contact"),
]