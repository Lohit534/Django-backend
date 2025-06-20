from django.shortcuts import render
from django.http import HttpResponse
from .models import post

# Create your views here.
def create(request):
    post.objects.create(
        post_id="AA1",
        content="first content",
        likes=0,
        user_id=3
    )
    return HttpResponse("created")



def get(request):
    res=post.objects.all()
    return res
