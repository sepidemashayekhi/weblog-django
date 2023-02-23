from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):    
    class Meta:
        model = Post
        fields = ['id','title', 'slug' , 'budy' , 'author']
        