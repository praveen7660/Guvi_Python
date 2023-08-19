# Lambda

# x  = lambda a,b:a+b
# print(x(5,30))

# Lambda Function inside a Function
# def f1(n):
#     return lambda a:a*n
#
# doub = f1(2)
# triple = f1(3)

# print(doub(11))
# print(triple(11))

#---------------------------------------------------
# Filter Functions

def prime(x):
    for i in range(2,x):
        if x%i ==0:
            return False
        else:
            return True
# filter function need 2 things
# 1 => A Functions
# 2 => A sequence
# filtered = filter(prime, range(10))

# print("Prime Numbers are :", list(filtered))

# --------------------------------------------------------
# MAP Needs 2 things Function and Iterables

def square(x):
    return x*x

numbers = [1,2,3,4,5]

Square_List = map(square,numbers)
print(list(Square_List))