from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import *
from .serializers import UserSerializer

# class UserList(generics.ListCreateAPIView):
# 	def get_queryset(self):
# 		queryset = Users.objects.all()
# 		filter_backends = [SearchFilter]
# 		search_fields = ['role','location']
# 		return queryset
# 	serializer_class = UserSerializer
class UserList(generics.ListCreateAPIView):
	
	queryset = Users.objects.all()
	filter_backends = [SearchFilter]
	search_fields = ['role','location']
	serializer_class = UserSerializer
	# return queryset