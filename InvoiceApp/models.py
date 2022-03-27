from django.db import models


class Invoice(models.Model):
    """Simple Invoice for Eastridge challenge."""
    created_date = models.DateField()

    def __str__(self):
        return f'Invoice, Created: {self.created_date}'


class InvoiceItem(models.Model):
    """Simple InvoiceItem for Eastridge challenge."""
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    units = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return f'Invoice: {self.invoice}, Units: {self.units}, Amount: {self.amount}, Description: {self.description}'


