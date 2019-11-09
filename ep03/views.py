from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from .models import Post
from .serializers import PostModelSerializer

# APIView를 활용한 내용 보기 CBV
'''class PostListAPIView(APIView):
    def get(self, request):
        serializer = PostModelSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostModelSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)'''

# APIView에서는 직접 Serializer를 처리를 해줬어야했다.
# 그런데 여러 Serializer에 대해서 구현을 하다보면 필연적으로 중복이 발생하게 된다. 이를 다음과 같이 mixins을 활용하여 줄여본다.
class PostListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# APIView를 활용한 내용 응답/수정/삭제 처리하는 CBV
# /post/10/ => GET, PUT, DELETE
'''class PostDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostModelSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializier = PostModelSerializer(post, data=request.data)
        if serializier.is_valid():
            serializier.save()
            return Response(serializier.data)
        return Response(serializier.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=204)'''

class PostDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
