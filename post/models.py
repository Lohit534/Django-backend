from django.db import models

# Create your models here.


class post(models.Model):
    post_id=models.CharField()
    content=models.TextField()
    likes=models.IntegerField()
    user_id=models.IntegerField()

    def __str__(self):
        return f"post_id={self.post_id}and content={self.content}"