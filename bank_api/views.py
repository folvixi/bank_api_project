from django.shortcuts import render

from rest_framework import viewsets
from .models import Client, Loan, Deposit
from .serializers import ClientSerializer, LoanSerializer, DepositSerializer

class ClientViewSet(viewsets.ModelViewSet):
    """
    ViewSet для клиентов
    обеспечивает все CRUD операции
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class LoanViewSet(viewsets.ModelViewSet):
    """
    ViewSet для кредитов
    """
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class DepositViewSet(viewsets.ModelViewSet):
    """
    ViewSet для вкладов
    """
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer