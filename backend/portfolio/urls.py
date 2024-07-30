from django.urls import path
from .views import (
    ProjectListView,
    StackListView,
    ResumeView,
    ProjectDetailView,
    CourseListView,
    ExperienceListView,
    SkillListView,
)


urlpatterns = [
    path("stacks/", StackListView.as_view(), name="stack-list"),
    path("courses/", CourseListView.as_view(), name="course-list"),
    path("skills/", SkillListView.as_view(), name="skill-list"),
    path("experiences/", ExperienceListView.as_view(), name="experience-list"),
    path("resume/", ResumeView.as_view(), name="resume"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/<slug:slug>/", ProjectDetailView.as_view(), name="project-detail"),
]
