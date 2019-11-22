from django.db import models
import uuid
# Create your models here.

# Branch model

class Branch(models.Model):
    location_name = models.CharField(
        max_length=30,
        unique=True,
    )


class Branch(models.Model):
    location_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    location_id = str(uuid.uuid4())

    def __str__(self):
        return f"{self.location_name} - {self.location}"



# Customer model
class Customer(models.Model):
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE
    )
    customer_name = models.CharField(max_length=30)
    customer_email = models.EmailField(max_length=300)

    def __str__(self):
        return f"{self.customer_name} - {self.branch}"

# Account model
class Account(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE
    )
    account_id = str(uuid.uuid4())

# Product model
class Product(models.Model):
    option_types = (
        ('checking', 'CHECKING'),
        ('savings', 'SAVINGS'),
        ('debit', 'DEBIT'),
        ('credit', 'CREDIT')
    )

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )

    product_type = models.CharField(
        max_length=8,
        choices=option_types,
        default=option_types[0]
    )
