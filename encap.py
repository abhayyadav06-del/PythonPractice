class Bank:
    # Constructor:  
    def __init__(self):
        # Double underscore (__) makes it private (name)
        self .__balance = 5000
        # Created a method to deposit money into the account
    def deposit(self, amount):
            # Add deposit money account 
            self .__balance += amount
            # Display the cureent balance 
    def show_balance(self):
            print(self .__balance)


            #Create an object (instance) of the Bank class

b = Bank()
b.deposit(6000)
b.show_balance()
