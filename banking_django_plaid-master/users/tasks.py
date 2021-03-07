from banking_django_plaid.celery import app
from plaid import Client
from .models import Tokens, Account
from celery import shared_task
import time

plaid_client_id = "5da9e9d3470e370016651aa3"
plaid_secret = "1026c23bcd23fccd4f9dabb1f9f172"

client = Client(client_id=plaid_client_id,
                      secret=plaid_secret,
                      environment='sandbox')


@shared_task
def saveTask(user, access_token):
    item_response = client.Item.get(access_token)
    institution_response = client.Institutions.get_by_id(item_response['item']['institution_id'], 'US')
    
    item_id = item_response['item']['item_id']
    webhook = item_response['item']['webhook']

    token = Tokens.objects.create(user=user, access_tkn=access_token, item_id=item_id, webhook = webhook)
    token.save()

@shared_task
def save_accounts_data(user, access_token):
    response = client.Accounts.get(access_token)
    accounts = response['accounts']
    count = 0
    for account in accounts:
        count += 1
        acc, is_created = Account.objects.get_or_create(user=user, name=account['name'], official_name=account['official_name'],
            account_id=account['account_id'], balance_available=account['balances']['available'], balance_current=account['balances']['current'],
            iso_currency_code=account['balances']['iso_currency_code'], limit=account['balances']['limit'], sub_type=account['subtype'], acc_type=account['type'],
            mask=account['mask'])
        if count>5:
            time.sleep(1)
            count = 0

@shared_task
def add(x, y):
    return x + y