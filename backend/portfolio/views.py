from .serializers import ExperienceSerializer, SkillSerializer, StackSerializer, ResumeSerializer, ProjectSerializer, CourseSerializer
from .models import Course, Experience, Project, Skill, Stack, Resume
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


class ExperienceListView(generics.ListAPIView):
    """
    Список опыта работы
    """

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class SkillListView(generics.ListAPIView):
    """
    Список навыков
    """

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class CourseListView(generics.ListAPIView):
    """
    Список курсов
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StackListView(generics.ListAPIView):
    """
    Список стеков
    """

    queryset = Stack.objects.all()
    serializer_class = StackSerializer


class ResumeView(APIView):
    """
    Метод для получения резюме
    """

    def get(self, request):
        queryset = Resume.objects.all().first()
        serializer = ResumeSerializer(queryset)

        return Response(serializer.data)


class ProjectListView(generics.ListAPIView):
    """
    Список проектов
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    """
    Подробная информация о проекте
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "slug"

    @extend_schema(summary="Подробная информация о проекте по слагу")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
