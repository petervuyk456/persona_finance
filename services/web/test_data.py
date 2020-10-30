from project.auth.models import User
from project.tracker.models import Entry, Account, CashFlow
import random
from datetime import datetime

random.seed(17)

usernames = ['holan',
             'eric',
             'john',
             'jacob',
             'jingleheimer',
             'schmidt']
accounts = {"401k": "asset",
            "403b": "asset",
            "457 Plan": "asset",
            "529": "asset",
            "IRA": "asset",
            "HSA": "asset",
            "FSA": "asset",
            "Brokerage": "asset",
            "Roth IRA": "asset",
            "Checking": "cash",
            "Savings": "cash",
            "Emergency Fund": "cash",
            "Credit Card": "debt",
            "Car Loans": "debt",
            "Student Loans": "debt",
            "Mortgage": "debt",
            "Loan Savings": "cash"}
cash_flows = {"Day Job": "income",
              "Side Hustle": "income",
              "Bonus": "income",
              "Rent": "expense",
              "Utilities": "expense",
              "Groceries": "expense",
              "Gasoline": "expense",
              "Insurance": "expense",
              "Auto Maintenance": "expense",
              "Phone": "expense",
              "Medical": "expense",
              "Pets": "expense",
              "Vacation/Travel": "expense",
              "Giving": "expense",
              "Eating Out": "expense",
              "Subscriptions": "expense",
              "Kids": "expense",
              "Misc": "expense"}


def generate_users(logger=None, force=False):
    
    if User and not force:
        return
    print('Resetting user collection')
    reset_db(User)
    print('Generating test users collection')

    # Create admin
    admin1 = User(username='smyth', role='admin')
    admin1.set_password('123456')
    admin1.save()

    def generate_history(obj, save_obj):
        for acct, type_ in obj.items():
            history = [Entry(value=random.randint(0, 10000),
                    entry_date=datetime(2020, val, 1))
                    for val in range(1, 11)]
            subobj = Account(name=acct, acct_type=type_, history=history)
            save_obj.append(subobj)

        return history

    user = []
    num_users = 5
    for i in range(num_users):
        user.append(User(username=usernames[i], role='user'))
        user[i].set_password('123456')

        # random account net worth values
        generate_history(accounts, user[i].worth)

        # random cash flow values
        generate_history(cash_flows, user[i].cash_flows)

        # commit save to Atlas
        user[i].save()

    # add everyone as a friend to each other
    for i in range(num_users):
        for j in range(num_users):
            if i != j:
                user[i].active_share.append(user[j].id)
                user[i].active_peek.append(user[j].id)
        user[i].save()


def reset_db(coll):
    coll.drop_collection()
