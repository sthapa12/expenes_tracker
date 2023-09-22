from django.urls import path
from apps.categories import views

urlpatterns = [
    path('user/<int;user_id>/create',views.CreateTransactionView.as_view(),name='create-transaction-user'),
    # path('list',views.ListUserView.as_view(),name='list-user')
]