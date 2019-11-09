from rest_framework import generics
from rest_framework import viewsets
from .models import Post
from .serializers import PostModelSerializer, UserSerializer
from django.contrib.auth import get_user_model

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

'''class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer



class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
'''

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

'''user_list = UserViewSet.as_view({
    'get': 'list',   # 호출될 함수와 호출할 함수를 지정한다.
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
})'''
