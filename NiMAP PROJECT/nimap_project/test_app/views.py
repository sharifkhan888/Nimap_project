from django.shortcuts import render
from rest_framework.generics import  ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializer import User,UserSerializer,Client,ClientSerializer,Project,ProjectSerializer

class ListCreateUser(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
 
 
class RUDUser(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class ListCreateClient(ListCreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
 
 
class RUDClient(RetrieveUpdateDestroyAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer


class ListCreateProject(ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
 
 
class RUDProject(RetrieveUpdateDestroyAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer