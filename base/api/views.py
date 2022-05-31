from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer, ProfileSerializer, CompanySerializer, JobSerializer
from base.models import Post, Profile, Company, JopOpening
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
def getPost(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getUsers(request):
    users = Profile.objects.all()
    serializer = ProfileSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRecommendedUsers(request):
    users = Profile.objects.filter(verified=True).order_by('?')
    serializer = ProfileSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request, username):
    user = Profile.objects.get(user__username=username)
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)  


@api_view(['GET'])
def getCompanies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)    


@api_view(['GET'])
def getCompany(request, pk):
    company = Company.objects.get(id=pk)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data)         


@api_view(['GET'])
def getJobs(request):
    jobs = JopOpening.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)  



