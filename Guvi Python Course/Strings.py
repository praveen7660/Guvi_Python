# strings

string = """
mai ek string hu
samjhe 
ka babu
"""
# print(string)

# An string is stored as ARRAY in python
x = "Hello World"
# print(x[10])

# for i in x:
#     print(i)

x = "Hello, From the World "
# print("From" in x)

# Slicing the string
print(x[2:5])
print(x[-5:-2])

print(x.lower())

# Strip the extra Spaces From the staring and ending of string
print(x.strip())

# Replace
print(x.replace("H","Y"))


# Split
print(x.split(","))

# Concatenate
a = "Hello"
b = "world"
print(a + " "+b)

# To get the Length
print(len(a))