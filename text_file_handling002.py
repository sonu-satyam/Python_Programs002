# **13 Program to print last "N" lines of a file.**
from itertools import islice
from collections import deque
# def last_ ( n ):
#     with open("new_file2.txt") as file:
#         count = 0
#         for item in file:
#             count = count +1
#         file.seek(0)
#         last_lines = islice(file,count-n,count+1)
#         for line in last_lines:
#             print(line)
#
#
# print(last_(1))

###############################################################################################
# **12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)**

# with open("new_file2.txt") as file:
#     for line_no,line in enumerate(file, start=1):
#         if line_no in range(1,5):
#             print(line_no,line)

###################################################################################################

# def last_line(n):
#     count = 0
#     with open("new_file2.txt") as file:
#         for line in file:
#             count+=1
#         file.seek(0)
#         last = islice(file,count-n,count+1)
#         for i in last:
#             print(i)
#
# last_line(9)

#################################################################################################
# **33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
# # Assume Below is the contents of the log file

# with open("new_file2.txt") as file:
#     d = {}
#     for line in file:
#         a=line.split(":")
#         if a[0] not in d:
#             d[a[0]]=1
#         else:
#             d[a[0]]=d[a[0]] + 1
#     print(d)

#####################################################################################################
# **53 Write a program to count the number of white spaces in a file.**
# with open("new_file2.txt") as file:
#     count = 0
#     for line in file:
#         for char in line:
#             if char == " ":
#                 count +=1
#     print(count)

##################################################################################################

# **71 Write a program to count the number of occurrences of each word in a file.**
# with open("new_file2.txt") as file:
#     d={}
#     for line in file:
#         words = line.split()
#         for word in words:
#             if word not in d:
#                 d[word]=1
#             else:
#                 d[word]+=1
#
#
# print(d)

########################################################################################################
# **72 Write a program to count the number of occurrences of vowels in a file.**
# with open("new_file2.txt") as file:
#     d={}
#     for line in file:
#         for word in line:
#             for char in word:
#                 if char in "aeiouAEIOU":
#                     if char not in d:
#                         d[char]=1
#                     else:
#                         d[char]+=1
#     print(d)

#########################################################################################
# **75 Write a program count the occurrence of a particular word in the file**

# def word_count(some_word):
#     count=0
#     with open("new_file2.txt") as file:
#         for line in file:
#             new_list = line.split()
#             for word in new_list:
#                 if word==some_word:
#                     count+=1
#         print(count)
#
# word_count("This")

#########################################################################################



























































































