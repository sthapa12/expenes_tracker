from apps.categories.models import Transaction
from rest_framework import serializers


class CreateTransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_date',
            'transaction_category',
        ]


class WithdrawTransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_date',
            'transaction_category',
        ]
