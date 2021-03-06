from django.db import models

from transactions.models import Transaction


class Currency(models.Model):
    name = models.CharField(max_length=25)
    contraction = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    @property
    def total(self):
        accounts = Account.objects.filter(currency=self)
        total = 0
        for a in accounts:
            total += a.balance
        return total

    @property
    def expenses(self):
        expenses = Transaction.objects.filter(transaction_type='o')
        transactions = expenses.filter(account__currency=self)
        total = 0
        for t in transactions:
            total += t.amount

        return total


class Account(models.Model):
    DEFAULT_CURRENCY_ID = 1  # pounds ?
    DEFAULT_OWNER = 1
    BANK = 'b'
    CASH = 'c'
    TYPE_CHOICES = (
        (BANK, 'Bank'),
        (CASH, 'Cash'),
    )
    account_type = models.CharField(max_length=5, choices=TYPE_CHOICES, default=CASH)
    bank_name = models.CharField(max_length=25, blank=True)
    number = models.CharField(max_length=140, blank=True)
    balance = models.DecimalField(decimal_places=2, max_digits=19, default=0.0)
    currency = models.ForeignKey(Currency, default=DEFAULT_CURRENCY_ID)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey('hubs.Hubs', default=DEFAULT_OWNER)

    def __str__(self):
        if self.account_type == 'b':
            return self.number
        else:
            return self.currency.name

    @property
    def expenses(self):
        transactions = Transaction.objects.filter(transaction_type='o')
        transactions = transactions.filter(account=self)
        total = 0
        for t in transactions:
            total += t.amount
        return total


class Transfer(models.Model):
    from_account = models.ForeignKey(Account, related_name="from_account")
    to_account = models.ForeignKey(Account, related_name="to_account")
    amount = models.DecimalField(decimal_places=2, max_digits=19)
    exchange_rate = models.DecimalField(decimal_places=2, max_digits=19)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount
