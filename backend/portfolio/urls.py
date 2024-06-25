from django.urls import  path
from .views import ProjectListView, StackListView, ResumeView


urlpatterns = [
    path('stacks/', StackListView.as_view(), name='stack-list'),
    path('resume/', ResumeView.as_view(), name='resume'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
]
