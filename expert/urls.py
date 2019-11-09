from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'expert'

router = DefaultRouter()
router.register(r'people', views.PeopleViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
