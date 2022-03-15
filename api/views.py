from rest_framework import viewsets
from posts.models import Post
from api.serializers import PostSerializer
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

    

    


