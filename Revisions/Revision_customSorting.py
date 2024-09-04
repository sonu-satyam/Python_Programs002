# sort based on lenth of items in descending order
names = ["apple", "google", "instagram", "facebook", "hp"]
def find_len(some_string):
    return len(some_string)
res = sorted(names,key=find_len , reverse=True)
# print(res)

#############################################################################

items = ["bv", "aw", "dt", "cu"]
def last_char(some_string):
    return some_string[-1]

last_=sorted(items,key=last_char)
# print(last_)
###################################################################################
temperatures = [("bangalore", 24), ("delhi",15), ("pune", 35), ("agra", 29)]
def low_temp(some_tuple):
    return some_tuple[1]
lowest = sorted(temperatures, key = low_temp)
# print(lowest)
##############################################################################
##FOR DISCTIONARY
share_prices = {"ACME":190, "AAPPLE":29, "HP":231, "SONY":210,"IBM":56}

key_value_pairs= share_prices.items()
def low_prices(item):
    return item[-1]
# print(dict(sorted(key_value_pairs, key=low_prices)))

##########################################################################
portfolio = [{"name":"IBM", "shares":100, "price":200},
             {"name":"INSTAGRAM", "shares":20, "price":20},
             {"name":"SONY", "shares":60, "price":180},
             {"name":"APPLE", "shares":10, "price":1200},
             {"name":"SAMSUNG", "shares":240, "price":210},
             {"name":"FB", "shares":91, "price":86.1}]

def get_price(some_dict):
    return some_dict["price"]

# print(sorted(portfolio,key = get_price))

students = [{"name": "john", "grade": "A", "age": 26},
            {"name": "jane", "grade": "B", "age": 28},
            {"name": "dave", "grade": "B", "age": 22}
            ]
def name(some_dict):
    return some_dict["name"]

# print(sorted(students,key=name))