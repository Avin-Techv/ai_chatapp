from django.shortcuts import render
import os
from django.conf import settings
from rest_framework.generics import GenericAPIView

from apps.users_management.serializers import RegisterSerializer,LoginSerializer
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate
from django.http import request

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ai_chatapp.settings")
# settings.configure()


# Create your views here.
class AuthUserAPIView(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self,request):
        user = request.user

        serializer = RegisterSerializer(user)


        return response.Response({"user":serializer.data})


class RegisterAPIView(GenericAPIView):
    authentication_classes=[]
    serializer_class = RegisterSerializer
    def post(self,request):
        
        serializer = self.serializer_class(data=request.data)         
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            errors = serializer.errors

        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    authentication_classes=[]

    serializer_class=LoginSerializer

    def post(self,request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)

        user = authenticate(username=email,password=password)


        if user:
            serializer = self.serializer_class(user)

            return response.Response(serializer.data,status=status.HTTP_200_OK)
        
        return response.Response({'message':"Invalid credentials, try agian"},status=status.HTTP_401_UNAUTHORIZED)




