from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from apps.categories import serializers
from rest_framework.exceptions import ValidationError
from apps.categories import models

User=get_user_model()

class CreateTransactionView(CreateAPIView):
    serializer_class=serializers.CreateTransactionSerializers
    
    def get_object(self):
        user_id=self.kwargs.get('user_id')
        try:
            user=User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            raise ValidationError({'Error':'user does not exist'})
    
    def perform_create(self, serializer):
        data=serializer.validated_data
        
        trasaction=models.Transaction.objects.create
        
            
    
# Create your views here.
