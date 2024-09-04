import csv
# path = r"C:\Users\Rudra\PycharmProjects\Program002\csv_filesnew_file001.csv"

# with open(path) as file:
#     reader_obj = csv.reader(file)
#
#     for row in reader_obj:
#         print(row)

# with open(path) as file:
#     dict_reader =csv.DictReader(file)
#
#     for row in dict_reader:
#         print(row)

###########################################
#writing into csv files

# path = r"C:\Users\Rudra\PycharmProjects\Program002\csv_files"

# with open(path + "demo001.csv", "w") as file:
#     writer_obj = csv.writer(file)
#
#     # writer_obj.writerow(["name", "age", "phone"])
#     # writer_obj.writerow(["steve", "18", "123456"])
#     data = [["steve", "18", "123456"], ["steve", "18", "123456"], ["steve", "18", "123456"]]
#     writer_obj.writerows(data)

# ######################################################################################################
# path = r"C:\Users\Rudra\PycharmProjects\Program002\csv_filesdemo002.csv"
#reader
# with open(path) as file:
#     _reader = csv.reader(file)
#     next(_reader)
#     for row in _reader:
#         if float(row[2]) > float(90):
#             print(row[0],row[2])

#dictreader
# with open(path) as file:
#     reader_ = csv.DictReader(file)
#     for row in reader_:
#         if float(row["price"]) > 90:
#             print(row["price"],row["name"])
############################################################
path = r"C:\Users\Rudra\PycharmProjects\Program002\csv_filesdemo001.csv"

# with open(path) as file:
#     reader_ = csv.DictReader(file)
#     dict_={}
#     for row in reader_:
#         if row["gender"] not in dict_:
#             dict_[row["gender"]]=row["name"]
#         else:
#             dict_[row["gender"]]+= row["name"]
#     print(dict_)
##########################################################
#gropu based on team

# with open(path) as file:
#     reader_ = csv.DictReader(file)
#     d = {}
#     for row in reader_:
#         if row["team"] not in d:
#             d[row["team"]]= row["name"] + " "
#
#         else:
#             d[row["team"]] += row["name"] + " "
#     print(d)
########################################################################################
#salary >70000
# with open(path) as file:
#     reader_ = csv.DictReader(file)
#     for row in reader_:
#         if int(row["pay"]) >7000:
#             print(row["pay"],row["name"])

############################################################
#sum to total vaccinations

path = r"C:\Users\Rudra\PycharmProjects\Program002\csv_filesnew_file001.csv"
#
# with open(path) as file:
#     reader_ = csv.DictReader(file)
#     sum = 0
#     for row in reader_:
#         if row["TOTAL_VACCINATIONS"]:
#             sum = sum + int(row["TOTAL_VACCINATIONS"])
#
#     print(sum)

#############################
#count no of countries

with open(path) as file:
    reader_ = csv.DictReader(file)
    count = 0
    for row in reader_:
        count +=1
        print(row["COUNTRY"],count)


































