from django.urls import path

from .views import BanksList, BankDetail, BanksInCity

urlpatterns = [
    path('banks/', BanksList.as_view(), name='list'),
    path('get_bank/', BankDetail.as_view(), name='detail'),
    path('get_branches/', BanksInCity.as_view(), name='banks_in_city')
]