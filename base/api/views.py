from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer, ProfileSerializer
from base.models import Post, Profile
from django.contrib.auth.models import User



@api_view(['GET'])
def getRoutes(request):
    routes = {
        'users': '/api/users',
        'posts/': '/api/posts/'
    }
    return Response(routes)

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUsers(request):
    users = Profile.objects.all()
    serializer = ProfileSerializer(users, many=True)
    return Response(serializer.data)




