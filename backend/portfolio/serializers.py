from rest_framework import serializers
from .models import Course, Experience, Project, Resume, Skill, Stack


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'
