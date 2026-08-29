from django.contrib.auth import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_blog, name='blog'),
    path("admin/", admin.site.urls),
]
