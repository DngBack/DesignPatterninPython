# SOLID - S 
# Sigle Responsibility Prnciples
# Each class only hase one responsibility
object_price = {
    "table": 10,
    "chair": 5, 
    "book": 3, 
    "pen": 1
}

# class BalanceBank:
#     def __init__(self): 
#         self.balance = 0 
    
#     def deposit(self, amount):
#         self.balance += amount
    
#     def withdraw(self, amount):
#         self.balance -= amount

#     def __get__(self):
#         return self.balance

#     def buying(self, object: str = ""):
#         if object in object_price:
#             if self.balance >= object_price[object]:
#                 self.withdraw(object_price[object])
#                 return f"You bought {object}"
#             else:
#                 return "Insufficient funds"
#         else:
#             return f"Object '{object}' is not available"
    
#     def sell(self, object: str = ""):
#         if object in object_price:
#             self.deposit(object_price[object])
#             return f"You sold {object}"
#         else:
            # return f"Object '{object}' is not available"
# It is not good based on the firt principle of Solid: Single Responsibility Princle 
class BalanceBank:
    def __init__(self): 
        self.balance = 0 
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def __get__(self):
        return self.balance

class BuyingWithAccount(BalanceBank):
    def buying(self, object: str = ""):
        if object in object_price:
            if self.balance >= object_price[object]:
                self.withdraw(object_price[object])
                return f"You bought {object}"
            else:
                return "Insufficient funds"
        else:
            return f"Object '{object}' is not available"

    def sell(self, object: str = ""):
        if object in object_price:
            self.deposit(object_price[object])
            return f"You sold {object}"
        else:
            return f"Object '{object}' is not available"
        
book_seller = BuyingWithAccount()
book_seller.sell("book")
print(book_seller.__get__())
