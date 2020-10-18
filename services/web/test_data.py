from project.auth.models import User
from project.tracker.models import Entry, Account, CashFlow
import random
from datetime import datetime

random.seed(17)

username = ['holan',
            'eric',
            'john',
            'jacob',
            'jingleheimer',
            'schmidt']

accounts = {'401k': 'asset',
            '403b': 'asset',
            '457 Plan': 'asset',
            '529': 'asset',
            'IRA': 'asset',
            'HSA': 'asset',
            'FSA': 'asset',
            'Standard Brokerage Acct': 'asset',
            'Roth IRA': 'asset',
            'Checking': 'cash',
            'Savings': 'cash',
            'Emergency Fund': 'cash',
            'Credit Card': 'debt',
            'Big Ticket Savings': 'cash',
            'Car Loans': 'debt',
            'Student Loans': 'debt',
            'Mortgage': 'debt',
            'Loan Savings': 'cash'}

cash_flows = {'Day Job': 'income',
              'Side Hustle': 'income',
              'Bonus': 'income',
              'Rent': 'expense',
              'Utilities': 'expense',
              'Groceries': 'expense',
              'Gasoline': 'expense',
              'Insurance': 'expense',
              'Auto Maintenance': 'expense',
              'Phone': 'expense',
              'Medical': 'expense',
              'Pets': 'expense',
              'Vacation/Travel': 'expense',
              'Giving': 'expense',
              'Eating Out': 'expense',
              'Subscriptions': 'expense',
              'Kids': 'expense',
              'Misc': 'expense'}


def generate_td():

    # Create admin
    admin1 = User(username='smyth', role='admin')
    admin1.set_password('123456')
    admin1.save()

    user = []
    for i in range(5):
        user.append(User(username=username[i], role='user'))
        user[i].set_password('123456')

        for acct, type_ in accounts.items():
            history = [Entry(value=random.randint(0, 10000),
                             entry_date=datetime(2020, val, 1))
                       for val in range(1, 11)]
            account = Account(name=acct, acct_type=type_, history=history)
            user[i].worth.append(account)

        for cf, type_ in cash_flows.items():
            history = [Entry(value=random.randint(0, 2000),
                             entry_date=datetime(2020, val, 1))
                       for val in range(1, 11)]
            account = CashFlow(name=cf, acct_type=type_, history=history)
            user[i].cash_flows.append(account)

        user[i].save()

    for i in range(5):
        for j in range(5):
            if i != j:
                user[i].active_share.append(user[j].id)
                user[i].active_peek.append(user[j].id)
        user[i].save()


def reset_db():
    User.drop_collection()
