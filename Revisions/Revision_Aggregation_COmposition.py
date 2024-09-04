class Demo:
    def method1(self):
        print("in demo class")

class Sample:
    def __init__(self):
        self.demo_obj = Demo()

    def method1(self):
        print("is sample class")

class Sample:

    def __init__(self,demo_obj):
        self.demo_obj = demo_obj

    def method1(self):
        print("in Sample class")

######################################################################
class ConsoleLogger:

    def log(self,message):
        print(message)

class FilteredLogger:

    def __init__(self,pattern,console_obj):
        self.pattern = pattern
        # self.console_obj = ConsoleLogger()
        self.console_obj = console_obj

    def log(self,message):
        if self.pattern in message:
            self.console_obj.log(message)



# obj=ConsoleLogger()
# d = FilteredLogger("hello",obj)
# d.log("hello there")

######################################################################
class TextFileLogger:
    def __init__(self,file_object):
        self.file_object = file_object

    def log(self,message):
        self.file_object.write(message)

class FilteredLogger:
    def __init__(self,pattern,logger_obj):
        self.pattern = pattern
        self.logger_obj = logger_obj

    def log(self,message):
        if self.pattern in message:
            self.logger_obj.log(message)


file = open("demo1.txt","w")
obj = TextFileLogger(file)
d=FilteredLogger("hello",obj)
# print(vars(d))
# print(vars(FilteredLogger))

d.log("heyy heyyyy java java java java python")
###########################################################################################################
# encapsulation

class Point:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __setattr__(self, key, value):
        if not isinstance(value,int):
            raise Exception("datatype not allowed")
        else:
            super().__setattr__(key,value)

    def __getattribute__(self, item):
        print(f"executing get attribute for item {item}")
        return super().__getattribute__(item)
#################################################################################
class Point:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __setattr__(self, key, value):
        if value < 0:
            raise Exception("datatype not allowed")
        else:
            super().__setattr__(key,value)

# p = Point(10,15)
# print(vars(p))

###########################################################################
class Employee:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay

    def __setattr__(self, key, value):
        if key == "name":
            if len(value) < 4:
                raise Exception("amount not allowed")
        elif key == "pay":
            if value < 1000:
                raise Exception("not allowed")
        super().__setattr__(key,value)

# e = Employee("steve",1200)
# print(vars(e))
##############################################################################
#getters and setters

class Demo:

    def __init__(self,a):
        self.a = a

    @property
    def a(self):
        return self._a

    @a.getter
    def a(self):
        pass

    @a.setter
    def a(self,value):
        if not isinstance(value,int):
            raise Exception("only int allowed")
        self._a = value
    @a.deleter
    def a(self):
        del self._a

d= Demo(10)
print(vars(d))





