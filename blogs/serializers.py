from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    
    created_by = serializers.StringRelatedField(read_only=True)
    category_name = serializers.ReadOnlyField(source="category.name")
    class Meta:
        model = Post
        fields = ['id','created_by', 'created_on','title', 'content', 'category','category_name', 'reading_time', 'image']
  

class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    category_name = serializers.ReadOnlyField(source="category.name")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


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

