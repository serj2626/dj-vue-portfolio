from rest_framework import serializers
from .models import Course, Experience, Project, Resume, Skill, Stack


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ("title",)


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    stack = StackSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"
