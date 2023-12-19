from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.views import View
from rest_framework import viewsets, pagination
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.db.models import Count



# Create your views here.

class PostViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PostDetailsViewSet(RetrieveUpdateDestroyAPIView, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'limit'  # Change the page size using 'limit' query parameter
    max_page_size = 100  # Maximum page size

class PostListView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-pk')
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset


class LatestPostsView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


    def list(self, request):
        latest_posts = Post.objects.all().order_by('-created_on')[:15]
        serializer = BlogSerializer(latest_posts, many=True)
        return Response(serializer.data)

class MostLikedPostsView(viewsets.ViewSet):
    def list(self, request):
        most_liked_posts = (
            Post.objects.annotate(like_count=Count('likes'))
            .order_by('-like_count')[:10]  # Fetch the top 10 most liked posts
        )
        serializer = BlogSerializer(most_liked_posts, many=True)
        return Response(serializer.data)

class CommentViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailsViewSet(RetrieveUpdateDestroyAPIView, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class CategoryViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailsViewSet(RetrieveUpdateDestroyAPIView, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ContactUsViewSet(ListCreateAPIView, GenericViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class ContactUsDetailsViewSet(RetrieveUpdateDestroyAPIView, GenericViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class ContactEmailViewSet(ListCreateAPIView, GenericViewSet):
    queryset = ContactEmail.objects.all()
    serializer_class = ContactEmailSerializer



class ContactEmailDetailsViewSet(RetrieveUpdateDestroyAPIView, GenericViewSet):
    queryset = ContactEmail.objects.all()
    serializer_class = ContactEmailSerializer


