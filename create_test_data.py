import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank_project.settings')
django.setup()

from bank_api.models import Client, Loan, Deposit

print("Создание тестовых данных...")

# очищаем старые данные
Client.objects.all().delete()

# создаем 5 клиентов
for i in range(1, 6):
    client = Client.objects.create(
        full_name=f'Клиент {i}',
        birth_date=date(1990, 1, i),
        passport=f'1234-56789{i}',
        phone=f'+7916123456{i}'
    )
    
    # создаем кредит для клиента
    Loan.objects.create(
        client=client,
        amount=100000 * i,
        interest_rate=10.5 + i/10,
        term_months=12 * i,
        start_date=date.today(),
        status='active',
        monthly_payment=10000 * i
    )
    
    # создаем вклад для клиента
    Deposit.objects.create(
        client=client,
        amount=50000 * i,
        interest_rate=5.5 + i/10,
        term_months=6 * i,
        start_date=date.today(),
        status='active'
    )
    
    print(f'Создан клиент {i} с кредитом и вкладом')

print("Тестовые данные созданы успешно!")