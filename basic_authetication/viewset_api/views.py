from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
# Create your views here.
from .models import StudentModel
from .serializers import StudentSerializer
class StudentModelViewset(viewsets.ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]
    