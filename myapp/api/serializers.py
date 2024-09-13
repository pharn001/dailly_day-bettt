from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6 , write_only=True)
    password2 =serializers.CharField(max_length=68, min_length=6 , write_only=True)

    class Meta:
        model = BlogPost
        fields = ['email', 'first_name', 'last_name', 'password','password2']
        
    def validate(self, attrs):
        return super().validate(attrs)
    def create(self, validated_data):
        return super().create(validated_data)