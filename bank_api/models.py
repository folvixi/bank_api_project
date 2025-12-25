from django.db import models

from django.db import models

class Client(models.Model):
    """
    модель клиента банка
    """
    full_name = models.CharField(max_length=100, verbose_name='полное имя')
    birth_date = models.DateField(verbose_name='дата рождения')
    passport = models.CharField(max_length=20, unique=True, verbose_name='номер паспорта')
    phone = models.CharField(max_length=20, verbose_name='телефон')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Loan(models.Model):
    """
    модель кредита
    привязана к клиенту
    """
    LOAN_STATUS = [
        ('active', 'активен'),
        ('paid', 'погашен'),
        ('overdue', 'просрочен'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='loans', verbose_name='клиент')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма кредита')
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='процентная ставка')
    term_months = models.IntegerField(verbose_name='срок в месяцах')
    start_date = models.DateField(verbose_name='дата начала')
    status = models.CharField(max_length=20, choices=LOAN_STATUS, default='active', verbose_name='статус')
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='ежемесячный платеж')

    def __str__(self):
        return f"Кредит {self.client}: {self.amount}"

    class Meta:
        verbose_name = 'кредит'
        verbose_name_plural = 'кредиты'


class Deposit(models.Model):
    """
    модель вклада
    привязана к клиенту
    """
    DEPOSIT_STATUS = [
        ('active', 'активен'),
        ('closed', 'закрыт'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='deposits', verbose_name='клиент')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма вклада')
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='процентная ставка')
    term_months = models.IntegerField(verbose_name='срок в месяцах')
    start_date = models.DateField(verbose_name='дата начала')
    status = models.CharField(max_length=20, choices=DEPOSIT_STATUS, default='active', verbose_name='статус')

    def __str__(self):
        return f"Вклад {self.client}: {self.amount}"

    class Meta:
        verbose_name = 'вклад'
        verbose_name_plural = 'вклады'