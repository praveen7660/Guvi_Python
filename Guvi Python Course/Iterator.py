# Iterable Vs Iterator

# Iterable = List, tuples and dict(this are iterable objects)

tuple1 = ("car","bike","train")
tuple2 = "Apple"
myit = iter(tuple1)
myit2 = iter(tuple2)

# print(next(myit2))
# print(next(myit2))
# print(next(myit2))
# print(next(myit2))
# print(next(myit2))

# same using loops
# for x in tuple1:
#     print(x)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a +=1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))