from django.contrib import admin
from django.urls import path

from menu import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about/", views.index, name="about"),
    path("about/team/", views.index, name="about-team"),
]
