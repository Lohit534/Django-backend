from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_id = models.CharField(max_length=20)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    




