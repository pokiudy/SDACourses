def validate_api(card_nr, pin):
    # validate account nr and pin
    # return true or false
    return True


class Card:
    def __init__(self, accounts=None):
        self.accounts = accounts

    def select_account(self, account_nr):
        print("----------",self.accounts)
        return next((account for account in self.accounts if account.account_nr == account_nr), None)
    # next arunca urmatorul item din lista


class Account:
    def __init__(self, account_nr, starting_balance=0):
        self.account_nr = account_nr
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class ATM:
    def __init__(self, ):
        self.card_inserted = False
        self.card_validated = False
        self.current_account = None
        self.current_card = None

    def validate_card_and_pin(self):
        if self.card_validated != True:
            raise RuntimeError("Card not validated")
        if not self.card_inserted:
            raise RuntimeError("Card not inserted")

    def insert_card(self, bank_card):
        self.card_inserted = True
        self.current_card = bank_card

    def eject_card(self):
        self.end_session()

    def validate_pin(self, pin):
        if not self.card_inserted:
            raise RuntimeError("Card not validated")
        self.card_validated = validate_api(card_nr=0, pin=0)
        return self.card_validated

    def select_account(self, account_nr):
        self.validate_card_and_pin()
        if self.current_card is None:
            raise RuntimeError("no card in ATM")
        current_account = self.current_card.select_account(account_nr)
        self.current_account = current_account

    def perform_request(self, request, amount=0):
        """
         1 = check
        balance
        2 = deposit
        money
        3 = withdraw
        money

        """

        if request == 1:
            return self.check_balance()
        elif request == 2:
            return self.accept_cash(amount)
        elif request == 3:
            return self.give_out_cash(amount)
        else:
            raise RuntimeError("invalid request")

    def accept_cash(self, amount):
        self.current_account.deposit(amount)
        return amount

    def give_out_cash(self, amount):
        self.current_account.widraw(amount)
        return amount

    def check_balance(self):
        return self.current_account.balance

    def end_session(self):
        self.card_inserted = False
        self.card_validated = False
        self.current_account = None
        self.current_card = None
        return True


my_account = Account("RDF1267399", 10)
accounts = [my_account]
my_card = Card(accounts=accounts)

atm = ATM()

#  1 = check
# balance
# 2 = deposit
# money
# 3 = withdraw
# money
atm.insert_card(my_card)
atm.validate_pin(1234)
atm.select_account("RDF1267399")

print(atm.perform_request(1))
print(my_account.balance)
print(atm.perform_request(2,amount=200))
print(my_account.balance)