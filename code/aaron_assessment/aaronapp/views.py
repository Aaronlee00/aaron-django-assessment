from django.shortcuts import render
from rest_framework import viewsets

from .serializers import DataSerializer
from .models import Data


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all().order_by('user_ID')
    serializer_class = DataSerializer
