from rest_framework import serializers
from .models import Client, Loan, Deposit

class ClientSerializer(serializers.ModelSerializer):
    """
    сериализатор для клиента
    преобразует модель в JSON
    """
    class Meta:
        model = Client
        fields = '__all__'  # все поля модели


class LoanSerializer(serializers.ModelSerializer):
    """
    сериализатор для кредита
    """
    class Meta:
        model = Loan
        fields = '__all__'


class DepositSerializer(serializers.ModelSerializer):
    """
    сериализатор для вклада
    """
    class Meta:
        model = Deposit
        fields = '__all__'