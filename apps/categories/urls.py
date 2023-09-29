from django.urls import path
from apps.categories import views

urlpatterns = [
    path('user/<int:user_id>/load',
         views.LoadTransactionsView.as_view(),
         name='create-transaction-user'
         ),
    path('user/<int:user_id>/withdraw',
         views.WithDrawTransactionsView.as_view(),
         name='withdraw-transaction-user'
         ),
]
