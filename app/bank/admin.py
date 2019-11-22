from django.contrib import admin
from bank.models import Branch, Customer, Account, Product

# Register your models here.

class CustomerInline(admin.TabularInline):
  model = Customer

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
  inlines = [
    CustomerInline
  ]

class AccountInline(admin.TabularInline):
  model = Account

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
  inlines = [
    AccountInline
  ]