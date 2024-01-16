from django.shortcuts import render
from .serializers import StudentSerializers
from .models import StudentModel 
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.authentication import BasicAuthentication
# Create your views here.
from rest_framework import viewsets
class StudentModelAdminView(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]

