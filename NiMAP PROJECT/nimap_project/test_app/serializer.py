from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client,Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']  
        

class ClientSerializer(serializers.ModelSerializer):
    #created_by=UserSerializer(read_only=True)
    #projects = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model=Client
        fields='__all__'   
        

class ProjectSerializer(serializers.ModelSerializer):
    #created_by=UserSerializer(read_only=True)
    #users = UserSerializer(many=True, read_only=True)
    #client=ClientSerializer(read_only=True)

    class Meta:
        model=Project
        fields='__all__'  