# **11. Write program to read a random line in a file. (ex. 50, 65, 78th line)**
# def func_(a):
#     with open("file3.txt") as file:
#         for lineno,line in enumerate(file ,start=1):
#             if lineno == a:
#                 print(line)
# func_(1)

################################################################################################
# **12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)**
# def range_(start,end):
#     with open("file3.txt") as file:
#         for lineno,line in enumerate(file, start=1):
#             if lineno in range(start, end+1):
#                 print(lineno,line)
#
# range_(3,6)

# from itertools import islice
# file = open("file3.txt")
# data = islice(file, 2)
# for item in data:
#     print(item)

########################################################################
# **13 Program to print last "N" lines of a file.**
from itertools import islice

# with open("file3.txt") as file:
#     count = 0
#     for _ in file:
#         count = count+1
#     file.seek(0)
#     data = islice(file, count - 2, count )
#     print(list(data))

##################################################################################
# **33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
# # Assume Below is the contents of the log file

# with open("file1.txt") as file:
#     dict_ = {}
#     for line in file:
#         l = line.split(":")
#         if l[0] not in dict_:
#             dict_[l[0]] = 1
#         else:
#             dict_[l[0]] +=1
#     print(dict_)


#############################################################################################
# **47 Count number of lines in a file without loading the file to the memory**

# with open("file1.txt") as file:
#     count = 0
#     for _ in file:
#         count = count +1
#
#     print(count)
#################################################################################################
# **48 Printing line and line no's**
# with open("file1.txt") as file:
#     for lineno,line in enumerate(file, start=1):
#         print(lineno,line)
#######################################################################################################
# **53 Write a program to count the number of white spaces in a file.**

# with open("file1.txt") as file:
#     count = 0
#     for line in file:
#         for char in line:
#             if char == " ":
#                 count +=1
#     print(count)

##################################################################################################
# **53 Write a program to count the number of white spaces in a file.**

# with open("file3.txt") as file:
#     dict_ = {}
#     for line in file:
#         l = line.split()
#         for word in l:
#             if word not in dict_:
#                 dict_[word]=1
#             else:
#                 dict_[word]+=1
#     print(dict_)


###########################################################################################################
# **72 Write a program to count the number of occurrences of vowels in a file.**

# with open("file3.txt") as file:
#     dict_ = {}
#     for line in file:
#         for char in line:
#             if char in "aeiouAEIOU":
#                 if char not in dict_:
#                     dict_[char]=1
#                 else:
#                     dict_[char]+=1
#     print(dict_)

##############################################################################################################
# **75 Write a program count the occurrence of a particular word in the file**

# with open("file1.txt") as file:
#     dict_={}
#     for line in file:
#         words= line.split()
#         for word in words:
#             if word not in dict_:
#                 dict_[word]=1
#             else:
#                 dict_[word]+=1
#     print(dict_)

##########################################################################################################
# **83 Write a program to count the number of commented lines in a text file**

# with open("file1.txt") as file:
#     count=0
#     for line in file:
#         if line.startswith("#"):
#             count+=1
#     print(count)

########################################################################################################
# **110 Replace all occurrences of "Java" with "Python" in a file**

#******in diff file

# with open("file3.txt") as read_file:
#     with open("file4.txt" , "w") as write_file:
#         for line in read_file:
#             new = line.replace("java","python")
#             write_file.write(new)


######## in same file

# with open("file3.txt", "r+") as file:
#     list_ = []
#     for line in file:
#         updated = line.replace("java", "python")
#         list_.append(updated)
#     file.seek(0)
#     file.writelines(list_)


#####################################################################################################3
# **153 write unique characters to the file**
word = "aaabbbccc"

w = set(word)

with open("unique.txt","w") as file:
    for word in w:
        file.write(word + "\n")























































































































