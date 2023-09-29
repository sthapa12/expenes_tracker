from django.contrib import admin
from apps.categories.models import Transaction


# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'transaction_type', 'transaction_date', 'current_balance']


admin.site.register(Transaction, TransactionAdmin)
