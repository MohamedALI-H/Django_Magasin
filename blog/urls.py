from django.urls import path,include
from . import views
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, PostDetailView


urlpatterns = [
      path('', PostListView.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
]

