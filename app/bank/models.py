from django.db import models
import uuid
# Create your models here.

# Branch model
class Branch(models.Model):
    location_name = models.CharField(max_length=30)
    location = models.CharField(max_lenght=30)
    location_id = str(uuid.uuid4())

    def __str__(self):
        f"{location_name} - {location}"

# Customer model
class Customer(models.Model):
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE
    )
    customer_name = models.CharField(max_length=30)
    customer_email = models.EmailField(max_length=300)

# Product model
class Product(models.Model):
    option_types - (
        ('checking', 'CHECKING'),
        ('savings', 'SAVINGS'),
        ('debit', 'DEBIT'),
        ('credit', 'CREDIT')
    )

    account_type = models.CharField(
        max_length=8,
        choices=option_types,
        default=option_types[0]
    )

# Account model
class Account(Product):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE
    )
    account_balance = models.FloatField(max_length=20)
