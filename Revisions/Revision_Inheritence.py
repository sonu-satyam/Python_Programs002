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

class SavingsAccount(BankAccount):
    interest_rate = 0.02
    def withdraw(self,amount):
        if amount > 10000:
            raise Exception("amount not allowed")
        super().withdraw(amount)

    def roi(self):
        super().roi()

# c1 = SavingsAccount("bob",10000)
# c1.deposit(11000)
# c1.withdraw(10000)
# c1.roi()
# print(vars(c1))
#################################################################################################
# LoggingInheritence

class ConsoleLogger:
    def log(self,message):
        print(message)

class TextFileLogger:

    def __init__(self,file_object):
        self.file_object = file_object

    def log(self,message):
        self.file_object.write(message)
        self.file_object.write("\n")

from csv import writer

class CsvFileLogger:
    def __init__(self,file_object):
        self.file_object = file_object

    def log(self,message):
        words = message.split()
        csv_writer = writer(self.file_object)
        csv_writer.writerow(words)


# file = open("demo2.csv", "w")
# logger = CsvFileLogger(file)
# logger.log("hello there how are you")
# logger.log("hello there how are you")
# logger.log("hello therre java is object oriented programming language")


# file = open("demo1.txt","w")
# logger = TextFileLogger(file)
# logger.log("hello python")
# logger.log("hello java")

class FilterConsoleLogger(ConsoleLogger):
    def __init__(self,some_message):
        self.some_message = some_message

    def log(self,message):
        if self.some_message in message:
            super().log(message)

# logger = FilterConsoleLogger("infy")
# logger.log("hello python info")

class FilteredTextLogger(TextFileLogger):
    def __init__(self,some_message,file_object):
        self.some_message = some_message
        super().__init__(file_object)

    def log(self,message):
        if self.some_message in message:
            super().log(message)
# file = open("demo1.txt","w")
# logger = FilteredTextLogger("info",file)
# logger.log("hello info hello")

class FilteredCSV(CsvFileLogger):
    def __init__(self,some_message,file_object):
        self.some_message = some_message
        super().__init__(file_object)

    def log(self,message):
        if self.some_message in message:
            super().log(message)

file = open("demo2.csv", "w")
logger = FilteredCSV("info",file)
logger.log("hello info hello python")
