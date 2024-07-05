from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.response import Response


class ContactCreateView(generics.CreateAPIView):
    """
    Создание сообщения
    """

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
