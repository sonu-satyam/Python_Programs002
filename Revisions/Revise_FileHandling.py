# print only the names of shares which has price > 90
import csv
# path = r"C:\Users\Rudra\PycharmProjects\Program002\csv_files\shares.csv"

# with open(path) as file:
#     reader_obj = csv.reader(file)
#     header = next(reader_obj)
#     for row in reader_obj:
#         if float(row[2]) > 90:
#             print(row[0])

# with open(path) as file:
#     reader_obj = csv.DictReader(file)
#     for row in reader_obj:
#         if float(row["price"]) > 90:
#             print(row["name"])
##############################################################################################################
# group the employees based on gender
# path= r"C:\Users\Rudra\PycharmProjects\Program002\csv_files\file1.csv"
#
# with open(path) as file:
#     reader_obj = csv.DictReader(file)
#     d = {}
#
#     for row in reader_obj:
#         if row["gender"] not in d:
#            d[row["gender"]] = row["name"] + " "
#         else:
#             d[row["gender"]] += row["name"] + " "
# print(d)
#########################################################
# group all the employees based on team
# path= r"C:\Users\Rudra\PycharmProjects\Program002\csv_files\file1.csv"
#
# with open(path) as file:
#     reader_obj = csv.DictReader(file)
#     d = {}
#     for row in reader_obj:
#         if row["team"] not in d:
#             d[row["team"]] = row["name"] + " "
#         else:
#             d[row["team"]] += row["name"] + " "

# print(d)
############################################################################################
# names of the employees whose salary is > 70000
# path= r"C:\Users\Rudra\PycharmProjects\Program002\csv_files\file1.csv"
#
# with open(path) as file:
#     reader_obj = csv.DictReader(file)
#     d = {}
#     for row in reader_obj:
#         if int(row["pay"]) > 70000:
#             print(row["name"])

#############################################################################################
# sum of total_vaccinations in vaccination_data.csv
# path = r"C:\Users\Rudra\PycharmProjects\Program002\csv_files\new_file.csv"
# with open(path) as file:
#     reader_obj = csv.DictReader(file)
#     total = 0
#     path = r"C:\Users\Rudra\PycharmProjects\Program002\csv_files\new_file.csv"
#     with open(path) as file:
#         reader_obj = csv.DictReader(file)
#             total += int(row["TOTAL_VACCINATIONS"])
# # print(total)

###################################################################################
# count the number of countries in vaccination_data.csv

path = r"C:\Users\Rudra\PycharmProjects\Program002\csv_files\new_file.csv"
with open(path) as file:
    reader_obj = csv.DictReader(file)
    count = 0
    for row in reader_obj:
        if row["COUNTRY"]:
            count+= 1
# print(count)











