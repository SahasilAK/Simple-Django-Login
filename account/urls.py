from django.urls import path
from account.views import account_view

app_name = 'account'

urlpatterns = [

   path('', account_view,name='account_view'),


]
