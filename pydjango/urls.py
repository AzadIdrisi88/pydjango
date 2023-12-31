from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.star),
    path("home/", views.home),
    path("radio/", views.radio),
    path("slct/", views.slct),
    path("chck/", views.chck),
    path("marksheet/", views.marksheet),
    path("capital/", views.capital),
    path("student/", views.student),
]
