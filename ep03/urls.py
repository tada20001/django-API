from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'post', views.PostViewSet)

add_name = 'ep03'

urlpatterns = [

    #path('post/', views.PostListAPIView.as_view()),
    #path('post/<int:pk>/', views.PostDetailAPIView.as_view()),
    
    #path('user/', views.user_list),
    #path('user/<int:pk>/', views.user_detail),
    path('', include(router.urls))
]
