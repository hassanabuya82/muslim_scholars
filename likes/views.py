from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *

class LikeViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class LikeDetailsViewSet(RetrieveUpdateDestroyAPIView, GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
