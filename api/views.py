from rest_framework import viewsets
from posts.models import Post, Comment
from api.serializers import CommentSerializer, PostSerializer
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    #queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()
        #serializer = PostSerializer(queryset, many=True)
        #return Response(serializer.data)

    #def retrieve(self, request, pk):
     #   return super().retrieve(request, pk)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()





    


