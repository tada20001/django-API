from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostModelSerializer

class PostListAPIView(APIView):
    def get(self, request):
        serializer = PostModelSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostModelSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
