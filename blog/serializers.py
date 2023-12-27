from rest_framework import serializers, viewsets
from .models import Comment
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CommentSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=200)
    created_date = serializers.DateTimeField()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('created_date', 'text')