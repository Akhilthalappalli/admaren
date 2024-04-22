from rest_framework import serializers
from .models import Tag, Snippet

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'
