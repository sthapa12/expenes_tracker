from apps.categories.models import Transaction
from rest_framework import serializers

class CreateTransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=[
            'currency',
            'amount',
            'transaction_date',
            'transaction_type',
            'transaction_category',
        ]