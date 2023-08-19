# List is Ordered, Changeable and allow duplicates
lists =['car','bike',30,4.0,50,True]
# print(lists[0])

# Range
# print(lists[2:5])

lists[4] = "Scooters"
# print(lists)

# Bike and 30 Get Replaced with Scooters and Watermelons
lists[1:3] = ["Scooters","watermelons"]

# print(lists)

# Insert At specific Location
lists.insert(3,"Jeep")
# print(lists)

# TUPLES
# ordered unchangeable and allow duplicates
z =('car','bike',30,4.0,50,True)
# print(type(tuple))
# print(len(tuple))

# print(z[:5])

# tuple.append("oranges")

# alternate method to add in tuple
x = list(z)
x[1] = "Oranges"
y = tuple(x)
# print(y)

# --------------------------------------------------
# Dictionaries
# unordered, changeable and do not allow duplicate values
dictt = {
    "name":"Raj",
    "age":13,
    "vechile":"Ford",
    "fruits":["Oranges","apples","guava"]
}
print(dictt)

# to get the length
print(len(dictt))

# To get the value of specific key
x = dictt["fruits"]
print(x)

# TO change for specific Key
dictt["vehicle"]="Bike"
print(dictt)

# How to remove
dictt.pop("vehicle")
print(dictt)