from django.db import models

class Budget(models.Model):
    number = models.CharField(max_length=100, unique=True)
    initial_date = models.DateTimeField()
    final_date = models.DateTimeField(blank=True)
    hub = models.ForeignKey('hubs.Hubs')

    def __str__(self):
        return self.number

class BudgetElement(models.Model):
    FIXED = 'f'
    VARIABLE = 'v'
    TYPE_CHOICES = (
            (FIXED, 'Fixed'),
            (VARIABLE, 'Variable'),
    )
    budget_type = models.CharField(max_length=5, choices=TYPE_CHOICES, default=FIXED)
    amount = models.DecimalField(decimal_places=2, max_digits=19, default=0)
    number = models.ForeignKey(Budget)
    currency = models.ForeignKey('accounts.Currency')
    category = models.ForeignKey('transactions.Category')
    #subcategory = models.ForeignKey('transactions.Subcategory', blank=True)
    
    """
    If the element is variable
    """
    FIRST_W = 'f'
    OTHER_W = 'o'
    V_TYPE_CHOICES = (
            (FIRST_W, 'First Week'),
            (OTHER_W, 'Other Week'),
    )
    variable_type = models.CharField(max_length=5, choices=V_TYPE_CHOICES, default=OTHER_W)

    def __str__(self):
        return str(self.amount)+":" + self.number.number

