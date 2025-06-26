from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView
from .views import BulkPostCreateView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
    path('bulk-create/', BulkPostCreateView.as_view(), name='bulk-post-create'),
]
