class Budget:
    def __init__(self, category,amount):
        self.category = category
        self.amount = amount
    def Deposit(self):
        return "This is The amount i want to deposit"
    def Check_balance(self):
        return "This is your balance"
    def Withdraw(self):
        return "This is the amount i want to withdraw"
    def Transfer_balance(self):
        return "Transfer the balance from clothing to food"
category = Budget("Clothing", 12000)
category_1 = Budget("Food", 10000)
category_2 = Budget("Entertainement", 5000)
print(category.Deposit())
print(category.Check_balance())
print(category.Withdraw())
print(category.Transfer_balance())


