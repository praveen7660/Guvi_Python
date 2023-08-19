# Class and Objects

# Simple  Structure
# class Human:
#     x = 5
#
# h1 = Human()
# print(h1.x)

# __init__() function is executed when a class is initialized

# self => referece to the current instantence of the class.
   # It is used to access this variable that belong to the class
class Human:
    def __init__(prvn, name, age):
        prvn.name = name
        prvn.age = age

    def methods(prvn):
        print("Hi My name is " + prvn.name)

h1 = Human("Sherlock",6)
# h2 = Human("Rahul",60)

# print(h1.name)
# print(h1.age)

h1.methods()
# h2.methods()

# Modifiy the values
h1.name = "Praveen"
h1.methods()

# Delete an object
del h1
