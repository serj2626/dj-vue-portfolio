from .serializers import StackSerializer, ResumeSerializer, ProjectSerializer
from .models import Project, Stack, Resume
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


class StackListView(generics.ListAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer


class ResumeView(APIView):
    def get(self, request):
        queryset = Resume.objects.all().first()
        serializer = ResumeSerializer(queryset)

        return Response(serializer.data)


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
