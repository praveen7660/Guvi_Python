# f = open("Trial.txt","r")
# print(f.read())
# print(f.readline())

# for x in f:
#     print(x)

# f.close()

# Opening File in append mode

# f = open("Trial.txt","a")
# f.write("This is New Line")
# f.close()

# f = open("Trial.txt","r")
# print(f.read())

# Opening File in write mode
# f = open("trial.txt","w")
# f.write("This Line Override the previous Info in the file as the file was opened in write mode")
# f.close()
#
# f = open("Trial.txt","r")
# print(f.read())

# In write mode you can open A file which doesn't exists. The python will create a file of that name for eg.'
# f = open("New_file_with_write.txt","w")

# Opening File in create new file

# f = open("New.txt","x")
# f.close()

# You can delete the files Too
import os
# os.remove("New.txt")
# os.remove("New_file_with_write.txt")