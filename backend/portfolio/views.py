from .serializers import StackSerializer, ResumeSerializer, ProjectSerializer
from .models import Project, Stack, Resume
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


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
