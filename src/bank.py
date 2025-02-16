from bank_account import BankAccount
from customer import Customer
from transaction import Transaction

class Bank:
    def __init__(self):
        self.accounts = {}
        self.customers = {}
        self.transactions = {}

    def create_account(self, account_number, customer_id):
        account = BankAccount(account_number)
        self.accounts[account_number] = account
        self.customers[customer_id] = Customer(customer_id, "John Doe")
        return account

    def process_transaction(self, transaction_id, account_number, amount):
        account = self.accounts[account_number]
        transaction = Transaction(transaction_id, account, amount)
        self.transactions[transaction_id] = transaction
        if amount > 0:
            account.deposit(amount)
        else:
            account.withdraw(-amount)