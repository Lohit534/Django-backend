from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

# Create your views here.

class UserView(ListView):
    def get(self, request):
        return HttpResponse("get method")
    
    def post(self, request):
        return HttpResponse("post method")
