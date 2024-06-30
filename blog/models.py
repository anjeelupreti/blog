
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    
    title = models.CharField(max_length=200,null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    content = models.TextField(null=False)
    add_date = models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{self.title}:{self.author}'