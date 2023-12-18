from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Like
        fields = '__all__'
