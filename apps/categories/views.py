from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, get_object_or_404

from apps.categories import models
from apps.categories import serializers

User = get_user_model()


class LoadTransactionsView(CreateAPIView):
    serializer_class = serializers.CreateTransactionSerializers

    def perform_create(self, serializer):
        # extract user id from url
        user_id = self.kwargs.get('user_id')
        # checking if user id is in db
        try:
            # get user instance
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValidationError({'Error': 'user does not exist'})
        data = serializer.validated_data  # data in dictionary form

        """
        suppose total balance gives currently 10000
        """

        transaction = models.Transaction(
            **data,
            transaction_type='Income',
            user=user,
            currency='USD'
        )
        current_balance = models.Transaction.objects.filter(user=user).count()
        if current_balance >= 1:
            last_balance = models.Transaction.objects.filter(
                user=user).order_by('-id')[0]
            transaction.current_balance = last_balance.current_balance + transaction.amount
        else:
            transaction.current_balance = transaction.amount
        transaction.save()


class WithDrawTransactionsView(CreateAPIView):
    serializer_class = serializers.WithdrawTransactionSerializers

    def perform_create(self, serializer):
        # Extract user id from the URL
        user_id = self.kwargs.get('user_id')

        # Check if the user exists
        user = get_object_or_404(User, id=user_id)

        # Retrieve the user's last transaction for checking the current balance
        last_transaction = models.Transaction.objects.filter(user=user).order_by('-id').first()

        # Calculate the available balance
        if last_transaction:
            available_balance = last_transaction.current_balance
        else:
            available_balance = 0

        # Get the withdrawal amount from the serializer data
        withdrawal_amount = serializer.validated_data['amount']

        # Check if the withdrawal amount is valid
        if withdrawal_amount <= 0:
            raise ValidationError({'Error': 'Invalid withdrawal amount'})

        # Check if the user's balance will remain above 100 after the withdrawal
        if available_balance - withdrawal_amount >= 100:
            transaction = models.Transaction(
                amount=withdrawal_amount,  # Withdrawal is a negative amount
                transaction_type='Expense',
                transaction_category=serializer.validated_data.get('transaction_category'),
                transaction_date=serializer.validated_data.get('transaction_date'),
                user=user,
                currency='USD',
            )
            transaction.current_balance = available_balance - withdrawal_amount
            transaction.save()
        else:
            raise ValidationError({'Error': 'Insufficient balance or atleast 100$ shall remain in bank'})
