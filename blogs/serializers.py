from rest_framework import serializers
from .models import *
from likes.serializers import LikeSerializer


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    category_name = serializers.ReadOnlyField(source="category.name")
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = '__all__'

    
    def get_comment_count(self, instance):
        return instance.comments.count()
    
    def get_like_count(self, instance):
        return instance.likes.count()
  

class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    category_name = serializers.ReadOnlyField(source="category.name")
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_comment_count(self, instance):
        return instance.comments.count()
    
    def get_like_count(self, instance):
        return instance.likes.count()

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'



class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = '__all__'


class ContactEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactEmail
        fields = '__all__'

