from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


@extend_schema(description="Создание сообщения")
class ContactCreateView(generics.CreateAPIView):
    """
    Представление для создания сообщения
    """

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
