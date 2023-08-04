from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *

# Create your views here.

class PostViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PostDetailsViewSet(RetrieveUpdateDestroyAPIView, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetailsViewSet(RetrieveUpdateDestroyAPIView, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class CategoryViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailsViewSet(RetrieveUpdateDestroyAPIView, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer