# blog/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    SignUpView, BlogListCreateView, BlogDetailView, MyBlogListView,
    CommentCreateView, CommentListView, ProfileListView, ProfileDetailView, ChangePasswordView
)

urlpatterns = [
    # Auth
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Blog URLs
    path('blogs/', BlogListCreateView.as_view(), name='blog_list_create'),
    # path('blogs/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('my_blogs/', MyBlogListView.as_view(), name='my_blog_list'),

    # Comments
    path('blogs/<int:blog_id>/comments/', CommentListView.as_view(), name='comment_list'),
    path('blogs/<int:blog_id>/comments/add/', CommentCreateView.as_view(), name='comment_create'),

    # Profile
    path('profiles/', ProfileListView.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('password/change/', ChangePasswordView.as_view(), name='change_password'),

]
