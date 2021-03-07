from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tokens(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    access_tkn = models.CharField(max_length = 200, default = None, null=True, blank=True)
    item_id = models.CharField(max_length = 200, default = None, null=True, blank=True)
    webhook = models.CharField(max_length = 200, default = None, null=True, blank=True)

class Account(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, default=None, null=True, blank=True)
	official_name = models.CharField(max_length=50, default=None, null=True, blank=True)
	account_id = models.TextField()
	balance_available = models.IntegerField(null=True, default=None)
	balance_current = models.IntegerField(null=True, default=None)
	iso_currency_code = models.CharField(max_length=10, default=None, null=True, blank=True)
	limit = models.IntegerField(default=None, null=True, blank=True)
	sub_type = models.CharField(max_length=10, default=None, null=True, blank=True)
	acc_type = models.CharField(max_length=10, default=None, null=True, blank=True)
	mask = models.CharField(max_length=10, default=None, null=True, blank=True)
