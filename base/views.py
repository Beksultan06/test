from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Test
from .serializers import TestSerializer

# Create your views here.
class TestAPIListCreate(ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer