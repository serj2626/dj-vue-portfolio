from django.urls import path
from .views import ProjectListView, StackListView, ResumeView, ProjectDetailView
from posts.views import PostListView, PostDetailView

urlpatterns = [
    path("stacks/", StackListView.as_view(), name="stack-list"),
    path("resume/", ResumeView.as_view(), name="resume"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/<slug:slug>/", ProjectDetailView.as_view(), name="project-detail"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
