class User:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
    
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}" )
    
    def make_deposit(self, amount):
        self.balance += amount
        return self

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.make_deposit(amount)
        return self

if __name__ == '__main__':
    kaija = User(10000, "Kaija")
    jonathan = User(8000, "Jonathan")
    juan = User(12000, "Juan")
    kaija.make_deposit(500).make_deposit(200).make_deposit(100).make_withdrawal(1000).display_user_balance()
    jonathan.make_deposit(600).make_deposit(150).make_withdrawal(400).make_withdrawal(150).display_user_balance()
    juan.make_deposit(500).make_withdrawal(150).make_withdrawal(1000).make_withdrawal(50).display_user_balance()
    kaija.transfer_money(juan, 5000).display_user_balance()
    juan.display_user_balance()

