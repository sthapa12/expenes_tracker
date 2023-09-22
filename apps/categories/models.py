from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User=get_user_model()

class Transaction(models.Model):
    CURRENCY_CHOICES =(
    ("USD", "USD"),
    ("EUR", "EUR"),
    ("GBP", "GBP"),
    ("YUAN", "YUAN"),
    ("AUD", "AUD"),)
    
    TRANSACTION_TYPE =(
    ("Income", "Income"),
    ("Expense", "Expense"))   
    
    TRANSACTION_CATEGORY =(
    ("Operation", "Operational"),
    ("Investment", "Investement"),
    ("Recurring", "Recurring"),
    ("Non-Recurring", "Non-Recurring"))
    
    
    currency=models.CharField(max_length=20,choices=CURRENCY_CHOICES,default="USD",null=True)
    amount=models.FloatField()
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    transaction_date=models.DateTimeField()
    created_date=models.DateTimeField(auto_now_add=True)
    transaction_type=models.CharField(max_length=20,choices=TRANSACTION_TYPE,null=True)
    transaction_category=models.CharField(max_length=20,choices=TRANSACTION_CATEGORY,null=True)    
    
    def __str__(self) -> str:
        return f'{self.user.fullname} available balance={self.amount}'
        