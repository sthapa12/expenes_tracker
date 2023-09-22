from rest_framework import serializers
from django.contrib.auth import get_user_model

User=get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password1=serializers.CharField()
    password2=serializers.CharField()
    
    class Meta:
        model=User
        fields=[
            'email',
            'fullname',
            'password1',
            'password2'
        ]
        
class ListUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=[
            'id',
            'email',
            'fullname',
            'is_active',
            'is_staff',
            'date_joined',
            'is_superuser',
        ]