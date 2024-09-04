import csv
# path = r"C:\Users\Rudra\PycharmProjects\Program002\csv_files\new_file.csv"
# for reader
# with open(path) as file:
#     obj_reader = csv.reader(file)
#     for item in obj_reader:
#         print(item[2])

#for Dictreader

# with open(path) as file:
#     obj_dict = csv.DictReader(file)
#     for item in obj_dict:
#         print(item["price"])

##############################################################################
#writer
# path = r"C:\Users\Rudra\PycharmProjects\Program002\csv_files"

# with open(path + "new_file002.csv" ,"w") as file:
#     writer_obj = csv.writer(file)

    # writer_obj.writerow(["name", "age", "salary"])
    # writer_obj.writerow(["harry", 15, 2000])
    # writer_obj.writerow(["peter", 25, 1000])
    # writer_obj.writerow(["john", 45, 9000])
    # data = [["name", "age", "salary"], ["harry", 15, 2000], ["peter", 25, 1000] ]
    # writer_obj.writerows(data)


###################################################################################
##dictwriter
# with open(path+ "new_file003.csv","w") as file:
#     writer_obj = csv.DictWriter(file,["a","b","c","d"])
#
#     writer_obj.writeheader()
#     # writer_obj.writerow({"a":1, "b":2, "c":3, "d":4})
#     # writer_obj.writerow({"a": 4, "b": 7, "c": 313, "d": 96})
#     # writer_obj.writerow({"a": 9, "b": 1, "c": 156, "d": 69})
#     # writer_obj.writerow({"a": 5, "b": 92, "c": 3, "d": 98})
#     # writer_obj.writerow({"a": 2, "b": 2, "c": 65, "d": 100})
#
#     data = [{"a":1, "b":2, "c":3, "d":4}, {"a": 4, "b": 7, "c": 313, "d": 96}, {"a": 9, "b": 1, "c": 156, "d": 69}, {"a": 2, "b": 2, "c": 65, "d": 100}]
#     writer_obj.writerows(data)

#########################################################################################################
##programs on csv file handling
# print only the names of shares which has price > 90

path = r"C:\Users\Rudra\PycharmProjects\Program002\csv_files\new_file.csv"

# with open(path) as file:
#     read_obj = csv.reader(file)
#     header = next(read_obj)# use the header first so that it cannot be iterated in for loop
#     for item in read_obj:
#         if float(item[1]) > 90:
#             print(item[0])

# with open(path) as file:
#     reader_obj = csv.DictReader(file)
#
#     for item in reader_obj:
#         if float(item["shares"]) >90:
#             print(item["name"])

###############################################################################################

# group the employees based on gender

# with open(path) as file:
#     male=[]
#     female=[]
#     obj_reader = csv.reader(file)
#     header = next(obj_reader)
#     for item in obj_reader:
#         if item[1] =="male":
#             male.append(item[0])
#         else:
#             female.append(item[0])
#     print(f"the male is {male}")
#     print(f"the female is {female}")


# with open (path) as file:
#     d = {}
#     read_obj = csv.DictReader(file)
#     for item in read_obj:
#         if item["gender"] not in d:
#             d[item["gender"]] = [item["name"]]
#         else:
#             d[item["gender"]] += [item["name"]]
#     print(d)

##################################################################################################
###### group all the employees based on team

# with open(path) as file:
#     d={}
#     read_obj = csv.DictReader(file)
#
#     for item in read_obj:
#         if item["team"] not in d:
#             d[item["team"]] = [item["name"]]
#         else:
#             d[item["team"]] += [item["name"]]
#     print(d)

##################################################################################################
#names of the employees whose salary is > 70000


#
# with open(path) as file:
#     d={}
#     read_obj = csv.DictReader(file)
#
#     for item in read_obj:
#         if int(item["pay"]) >70000:
#             d[item["name"]]= item["pay"]
#     print(d)


#############################################################################################
# sum of total_vaccinations in vaccination_data.csv
# with open(path) as file:
#     sum_vacc = 0
#     obj_reader = csv.DictReader(file)
#
#     for item in obj_reader:
#         if item["TOTAL_VACCINATIONS"]:
#             sum_vacc= sum_vacc + int(item["TOTAL_VACCINATIONS"])
#
# print(sum_vacc)


#######################################################################################
# count the number of countries in vaccination_data.csv

# with open(path) as file:
#     reader_obj = csv.DictReader(file)
#     count = 0
#     for item in reader_obj:
#         if item["COUNTRY"]:
#             count = count + 1
#     print(count)