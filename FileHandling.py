# # with open("file1.txt", "r") as f:
# #     for line_no,line in enumerate(f, start=1):
# #         if line_no==5:
# #             print(line)
#
# ##################################################################################################################
#
# with open("names.txt", "r") as f:
#     names_=[]
#     for item in f:
#         n = item.split()
#         names_.append(n[0])
#     print(names_)
# #
# # with open("new_file.txt", "w") as f1:
# #     for name in names_:
# #         f1.write(name)
# #         f1.write("\n")
#
# with open("new_file2.txt", "w") as f:
#     f.write("hello\n")
#     f.write("hiiiii\n")
#     f.write("python")

#######################################################################################################
# **33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
#
# with open("new_file2.txt", "r") as f:
#     new_dict = {}
#     for data in f:
#         msg,content= data.split(":")
#         if msg not in new_dict:
#             new_dict[msg] = 1
#         else:
#             new_dict[msg] +=1
# print(new_dict)

#####################################################################################################
###count the no of words in a file

# with open("new_file.txt", "r") as f:
#     count = 0
#     for words in f:
#         l_words = words.split()
#         count = count + len(l_words)
# print(count)

###########################################################################################################
##print line with line no from the file

# with open("new_file.txt","r") as f:
#     for line_no,line in enumerate(f, start=1):
#         print(line_no,line)


################################################################################################################
# with open("new_file.txt", "w") as f:
#     f.write("\nhello java\njava programming is fun\njava is easy to learn")

###############################################################################################
###copying file from another file

# with open("new_file.txt", "r") as f1:
#     with open("new_file2.txt", "w") as f2:
#         for words in f1:
#             f2.write(words)
####################################################################################################
# with open("new_file2.txt", "r") as f1:
#     with open("new_file.txt", "r") as f2:
#         for item1,item2 in zip(f1,f2):
#             print(item1,item2)

####################################################################################################################
# **11. Write program to read a random line in a file. (ex. 50, 65, 78th line)**

# with open("new_file.txt", "r") as f:
#     for line_no,line in enumerate(f, start=1):
#         if line_no == 2:
#             print(line_no,line)


#################################################################################################################

# **11. Write program to read a random line in a file. (ex. 50, 65, 78th line)**
# with open("new_file.txt", "r") as f:
#     for line_no,line in enumerate(f,start=1):
#         if line_no in range(3,6):
#             print(line_no,line)

####################################################################################################################
from itertools import islice
#
# def slice_file(start,end):
#     with open("new_file.txt", "r") as f:
#         a=islice(f,start,end+1)
#         for lines in a:
#             print(lines)
#
# print(slice_file(2,5))

####################################################################################################################
#####################################################################
# **13 Program to print last "N" lines of a file.**

# def slice_file(n):
#     with open("new_file.txt")as f:
#         count = 0
#         for line in f:
#             count = count + 1
#
#         f.seek(0)
#         a = islice(f, n, count+1)
#         for item in a:
#             print(item)
# slice_file(4)

###by using DEQUE
# from collections import deque
# def slice_last_ (n):
#     with open("new_file.txt") as f:
#         data = deque(f,n)
#
#         for line in data:
#             print(line)
# slice_last_(5)


###################################################################################################################
# **33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**


# with open("new_file2.txt") as f:
#     dict_new = {}
#     for lines in f:
#         new_line = lines.split(":")
#         key= new_line[0]
#         if key not in dict_new:
#             dict_new[key] = 1
#         else:
#             dict_new[key] = dict_new[key] +1
# print(dict_new)

#############################################################################
# **47 Count number of lines in a file without loading the file to the memory**

# with open("new_file2.txt") as f:
#     count = 0
#     for lines in f:
#         count+=1
# print(count)

######################################################################################
# **53 Write a program to count the number of white spaces in a file.**

#type1

# with open("names.txt") as f:
#     count_space =0
#     for line in f:
#         for char in line:
#             if char == " ":
#                 count_space +=1
# print(count_space)

#type 2
#
# with open("names.txt") as f:
#     count_space = 0
#     for line in f:
#         count_space += line.count(" ")
# print(count_space)

####################################################################################################
# **71 Write a program to count the number of occurrences of each word in a file.**
# with open("names.txt") as f:
#     dict_= {}
#     for char in f:
#         s_list = char.split()
#         for word in s_list:
#             if word not in dict_:
#                 dict_[word]=1
#             else:
#                 dict_[word] +=1
#
# print(dict_)

#######################################################################################################
# **72 Write a program to count the number of occurrences of vowels in a file.**
# d = {}
# with open("names.txt") as f:
#     for lines in f:
#         for char in lines:
#             if char in "aeiouAEIOU":
#                 if char not in d:
#                     d[char] = 1
#                 else:
#                     d[char] +=1
# print(d)







###############################################################################################################
# **75 Write a program count the occurrence of a particular word in the file**
# def word_count (key):
#     with open("new_file.txt") as f:
#         count =0
#         for line in f:
#             words= line.split()
#             for word in words:
#                 if word == key:
#                     count = count + 1
#     return count
# print(word_count("java"))


###################################################################################################
# **83 Write a program to count the number of commented lines in a text file**

# with open("new_file.txt") as f:
#     count = 0
#     for line in f:
#         if line.startswith("#"):
#             count +=1
# print(count)
#####################################################################################################

#**110 Replace all occurrences of "Java" with "Python" in a file**
# with open("names.txt") as f_read:
#     with open("names_new.txt", "w") as r_write:
#         for line in f_read:
#             updated_ = line.replace("java", "python")
#             r_write.write(updated_)
#********************

# with open("names_new.txt","r+") as f:
#     list_updated = []
#     for line in f:
#         up_line = line.replace("python", "java")
#
#         list_updated.append(up_line)
#     f.seek(0)
#     f.writelines(list_updated)

########################################################################################################
# **153 write unique characters to the file**
# word = "aaabbbccc"
#
# unique_char = set(word)
# with open("names_new.txt","w") as f:
#     f.writelines(unique_char)





















































































































