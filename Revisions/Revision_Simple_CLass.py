class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a/self.b

obj1 = Calculator(10,20)
obj2 = Calculator(20,5)

# print(obj1.div())
# print(Calculator.add(obj2))

########################################################################################################################
class Employee:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay

    def email(self):
        return f"{self.name}@company.com"
    def pay_hike(self,percent_hike):
        hike_amount = self.pay * percent_hike
        self.pay += hike_amount

e1=Employee("steve",1000)
e2 = Employee("jobs",1500)
# print(vars(e1))
# print(e1.pay_hike(0.1))
# print(vars(e1))
# print(e1.email())
# print(vars(e2))
# print(e2.pay_hike(0.1))
# print(vars(e2))
# print(e2.email())
####################################################################################################################
class BankAccount:
    interest_rate = 0.01
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.transaction = []

    def deposit(self,amount):
        self.balance = self.balance + amount
        self.transaction.append(f"the amount deposited {amount}")

    def withdraw(self,amount):
        if self.balance < amount:
            raise ValueError("amount not available")
        self.balance = self.balance - amount
        self.transaction.append(f"the amount withdrawn {amount}")

    def transfer(self,to_account,amount):
        if amount > self.balance:
            raise ValueError("Insufficient Funds")
        to_account.deposit(amount)
        self.balance = self.balance - amount
        self.transaction.append(f"the amount transfered {amount}")

    def statements(self):
        for item in self.transaction:
            print(item)
        print(f"the total balance is {self.balance}")

    def roi(self):
        interest_amt = self.balance * self.__class__.interest_rate
        self.balance = self.balance + interest_amt
        self.transaction .append(f"interest credited {interest_amt}")

c1= BankAccount("Bill",1000)
c2 = BankAccount("gates",10000)
# c1.deposit(100)
# c1.deposit(900)
# c1.transfer(c2,100)
# c2.deposit(500)
# c2.withdraw(250)
# print(c1.withdraw(300))
# c1.transfer(c2,60)
# c1.statements()
# print(vars(c1))
# print(vars(c2))
# c2.roi()
# c2.statements()

####################################################################################################################
class Shopping:
    products = {"iphone":5, "samsung":3, "oneplus":7, "vivo":1}
    prices = {"iphone":800, "samsung":700, "oneplus":500, "vivo":1000}

    def __init__(self):
        self.cart = []

    def add_item(self,name, quantity):
        if name not in self.__class__.products.keys():
            raise Exception("item not available")

        if quantity > self.__class__.products[name]:
            raise Exception("out of stock")

        item = {"name":name, "quantity":quantity, "price":self.__class__.prices[name]}
        self.cart.append(item)
        self.__class__.products[name] -= quantity

    def remove_item(self,name):
        for item in self.cart:
            if name == item["name"]:
                if item["quantity"]==1:
                    self.cart.remove(item)
                else:
                    item["quantity"] -= 1

    def cart_value(self,name):
        for item in self.cart:
            if name == item["name"]:
                return item["quantity"] * item["price"]

# cart1 = Shopping()
# cart1.add_item("iphone",3)
# print(cart1.__dict__)
# cart1.remove_item("iphone")
# print(cart1.__dict__)
# print(cart1.cart_value("iphone"))
#####################################################################################################################################################



















