from rest_framework import serializers
from .models import Language, Post, Tool

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ['name']

class PostSerializer(serializers.ModelSerializer):
    languages = serializers.StringRelatedField(many=True)
    tools = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = (
            'company',
            'logo',
            'new',
            'featured',
            'position',
            'role',
            'level',
            'posted_at',
            'contract',
            'location',
            'languages',
            'tools',
        )


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['name']

        