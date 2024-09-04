# find square of the list
numbers = [1,2,3,4,5,6,7]
res = [item **2 for item in numbers]
# print(res)
################################################################

# find even no from range of 1 to 50
res = [item for item in range(1,51)  if item % 2 == 0 ]
# print(res)

####################################################################
# make negative every numbers
numbers = [1,2,3,4,5,6]

res = [item * -1 for item in numbers]
# print(res)
#####################################################################
# create list from names that starts with vowels
names = ['laura', 'steve','aakash', 'bill', 'scott', 'mathews','andrews', 'bob', 'ive']
res = [item for item in names if item[0] in "aeiou" ]
# print(res)
# create list from names that starts with consonants
res = [item for item in names if item[0] not in "aeiou"]
# print(res)
#####################################################################
# filter only those letters starting with "P"
languages = ["Python", "Java", "Php", "JS", "C++", "Ruby", "Perl"]

res = [letters for letters in languages if letters[0] == "P"]
# print(res)
########################################################################
# make two list first list with first name and second list with last name
names = ["steve smith", "john doe", "bill gates"]
first_names =[name.split()[0] for name in names]
last_name = [name.split()[1] for name in names]
# print(first_names)
# print(last_name)
#######################################################################
# make a list of tuple having item and length pair
names = ['laura', 'steve','aakash', 'bill', 'scott', 'mathews','andrews', 'bob', 'ive']
res = [(item,len(item)) for item in names ]
# print(res)
######################################################################
from math import factorial
numbers = [1,2,3,4,5]
res = [factorial(item) for item in numbers]
# print(res)
#####################################################################
# reverse odd length character
names = ['laura', 'steve','aakash', 'bill', 'scott', 'mathews','andrews', 'bob', 'ive']
res = [item[::-1] if len(item) % 2 == 1 else item for item in names ]
# print(res)
##################################################################
# if item in string reverse else print as it is
data = ["hello", 16, 12.4, "world", "python"]
res = [item[::-1] if isinstance(item,str) else item for item in data]
# print(res)
#####################################################################
a=[1,2,3,4,5]
b=[6,7,8,9,10]
res = [n1 + n2 for n1,n2 in zip(a,b)]
# print(res)
###########################################################
# output should be all characters in a single list
matrix = [[1,2,3], [4,5,6], [7,8,9]]

res = [item for items in matrix for item in items]
# print(res)
############################################################
letters = "ABCDEFGH"
numbers = [0,1,2,3,4,5,6,7]
res = [(letter,number) for letter,number in zip(letters,numbers)]
# print(res)
############################################################################################
##DICT DISCTIONARY
# make word and lenth pair
sentence = "hello python hello world"
s_list = sentence.split()
d = {}
for item in s_list:
    d[item] = len(item)
# print(d)

res = {item:len(item) for item in s_list}
# print(res)

##########################################################################################
# make word count pair
sentence = "hello python hello world hello world hello python world"
s_list = sentence.split()
d = {}
for item in s_list:
    if item not in d:
        d[item] = 1
    else:
        d[item] +=1
# print(d)
########################
res = {item:s_list.count(item) for item in s_list}
# print(res)
####################################################################
# get character and its count pair
sentence = "hello python hello world hello world hello python world"
d = {}
for item in sentence:
    if item not in d:
        d[item] = 1
    else:
        d[item] += 1
# print(d)
#########################
res = {item:sentence.count(item) for item in sentence}
# print(res)
###########################################################################
# letter and ascii value pair
word = "abcde1234"
res = {letter:ord(letter) for letter in word}
# print(res)
##########################################################################
# make new dict and add marks with 10
students = {"steve":10, "eve":15, "mark":13}
new_dict = {}
for name,marks in students.items():
    new_dict[name] = marks + 10
# print(new_dict)
#################
res = {student:marks + 10 for student,marks in students.items()}
# print(res)
###############################################################################
# make a disctionary with city temperature pair from two list
cities = ["delhi", "tokyo", "bangalore", "noida"]
temperature = [45,21,23,42]
dict_pair = {}
for city,temp in zip(cities,temperature):
    dict_pair[city]=temp
# print(dict_pair)
#######################
res = {city:temp for city,temp in zip(cities,temperature)}
# print(res)
########################################################################
dial_codes = [(91,"india"), (7,"russia"), (68,"china")]
d = {}
# for item in dial_codes:
#     d[item[1]] = item[0]
# print(d)
####################################
res = { item[1]:item[0] for item in dial_codes }
# print(res)
####################################################################################
# create a new disctionary having share price more than 200
prices = {"ACME":26, "AAPL":201, "IBM":129, "META":298}
d={}
for share,price in prices.items():
    if price > 200:
        d[share] = price
# print(d)
##################
res = {share : price for share,price in prices.items() if price > 200}
# print(res)
#############################################################################################
#SET COMPREHENSION
# create a set having square of  nums
nums = [1,2,3,4,5,6,1,2,3,4]
# squares_=set()
#
# for item in nums:
#     squares_.add(item ** 2)
# print(squares_)
#
# res = {item ** 2 for item in nums}
# print(res)




























