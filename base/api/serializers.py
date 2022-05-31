from dataclasses import field
from rest_framework.serializers import ModelSerializer 
from base.models import Post, Profile, Company, JopOpening
from django.contrib.auth.models import User



class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id']       


class ProfileSerializer(ModelSerializer):
    user = UserSerializer(many = False)
    class Meta:
        model = Profile
        fields = '__all__'


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'        

class JobSerializer(ModelSerializer):
    class Meta:
        model = JopOpening
        fields = '__all__'           