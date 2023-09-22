from django.shortcuts import render
from rest_framework import generics
from apps.users.serializers import RegisterUserSerializer, ListUserSerializer
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

User=get_user_model()
# Create your views here.

class RegisterUserView(generics.CreateAPIView):
    serializer_class=RegisterUserSerializer
    queryset=''
    def perform_create(self, serializer):
        data=serializer.validated_data
        # import pdb
        # pdb.set_trace()
        
        password1=data.pop('password1')
        password2=data.pop('password2')
        if password1!=password2:
            raise ValidationError({'Error':'password did not match'})
        if len(password1)<=8:
            raise ValidationError({'Error':'password length must not be less than 8 character'})
        user=User.objects.create(email=data.get('email'),fullname=data.get('fullname'))
        user.set_password(password1)  #set_password menthod saves plain passowrd to hash password
        user.save()
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # data={
        #     'email':serializer.data.get('email'),
        #     'fullname':serializer.data.get('fullname'),
        #     'message':'User created successfully.'
        # }
        return Response(data='User created successfully.',status=status.HTTP_201_CREATED)    
    
class ListUserView(generics.ListAPIView):
    serializer_class=ListUserSerializer
    # queryset=User.objects.all()
    def get_queryset(self):
        return User.objects.all()
    
    