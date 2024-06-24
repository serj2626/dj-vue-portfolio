from .serializers import StackSerializer
from .models import Stack
from rest_framework import generics


class StackListView(generics.ListAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer
