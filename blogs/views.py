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
# Create your views here.

class PostViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PostDetailsViewSet(RetrieveUpdateDestroyAPIView, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer

    def list(self, request, *args, **kwargs):
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 1000))
        category_id = request.GET.get('category')

        start_index = (page - 1) * limit
        end_index = start_index + limit

        if category_id:
            blogs = self.queryset.filter(category=category_id)[start_index:end_index]
        else:
            blogs = self.queryset[start_index:end_index]  # Get paginated blogs
    
        serializer = self.get_serializer(blogs, many=True)
        data = serializer.data

        return Response({ 'blogs': data})
    
class CustomPagination(pagination.PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'limit'  # Change the page size using 'limit' query parameter
    max_page_size = 100  # Maximum page size

class PostListView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Post.objects.all()
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


