from rest_framework import serializers
from .models import Course, Experience, Project, Resume, Skill, Stack


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "title",
            "company",
            "description",
            "date_start",
            "date_end",
        )


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            "vacancy_title",
            "company",
            "responsibilities",
            "date_start",
            "date_end",
        )


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ("title", "img", "level", "slug")


class ProjectSerializer(serializers.ModelSerializer):
    stack = StackSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)
    stack = StackSerializer(many=True)
    experience = ExperienceSerializer(many=True)
    course = CourseSerializer(many=True)

    class Meta:
        model = Resume
        fields = (
            "name",
            "surname",
            "position",
            "stack",
            "skill",
            "course",
            "experience",
            "min_salary",
            "max_salary",
            "about",
            "github_url",
            "avatar",
            "get_avatar",
        )
