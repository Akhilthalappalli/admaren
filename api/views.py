from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from .models import Snippet, Tag
from .serializers import SnippetSerializer, TagSerializer
from rest_framework.permissions import IsAuthenticated


#create(post) Listing(Get)
class SnippetListCreateView(mixins.ListModelMixin,mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]
    

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # get total list with total snippet count
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        total_count = queryset.count()

        return Response({
            'total_count': total_count,
            'snippets': serializer.data
        })
    
# Update,retrieve,delete single data
class SnippetsDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
#create(post) Listing(Get)
class TagListCreateView(mixins.ListModelMixin,mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
# Update,retrieve,delete single data
class TagDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
