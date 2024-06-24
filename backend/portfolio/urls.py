from django.urls import  path
from .views import StackListView


urlpatterns = [
    path('stacks/', StackListView.as_view(), name='stack-list'),
]
