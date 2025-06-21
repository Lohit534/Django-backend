from django.db import models

# Create your models here.

class post(models.Model):
    user_name=models.CharField()
    user_id=models.TextField()
    email=models.EmailField()
    password=models.CharField(max_length=16)

    def __str__(self):
        return f"post_id={self.user_name}and content={self.user_id}"