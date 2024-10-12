from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(s):
        return s.name
    
class Project(models.Model):
    name=models.CharField(max_length=100)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    users=models.ManyToManyField(User,related_name="asign_users")
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)