from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializers


class PostList(APIView):
    
    
    def get_objects_(self):
        try:
            post  = Post.objects.all()
        except:
            raise Http404()
        return post
    
    def get(self,request):

        post = self.get_objects_()
        serializer = PostSerializers(post,many=True)

        return Response(serializer.data)
    
    def post(self,request):
        post = request.data
        print(post)




        





        


