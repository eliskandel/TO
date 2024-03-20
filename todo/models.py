from django.db import models
from user.models import User
# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=200,blank=False,null=False)
    completed=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
    
class Tag(models.Model):
    name=models.CharField(max_length=250,null=False)
    todo=models.ForeignKey(Todo,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
