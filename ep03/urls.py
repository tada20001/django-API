from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework.routers import DefaultRouter


add_name = 'ep03'

urlpatterns = [
    path('post/', views.PostListAPIView.as_view()),
]
