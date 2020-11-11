from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
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
    
    

