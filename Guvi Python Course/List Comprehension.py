fruits = ["apples","bananans","pineapple","kiwi"]

# newfruits=[]
#
# for x in fruits:
#     if "a" in x:
#         newfruits.append(x)

# similar thing using list comprehension

# newfruits = [x for x in fruits if "a" in x]
# newfruits = [x for x in fruits if x !="bananans"]
# newfruits = [x for x in range(10)
# ]
# newfruits = [x.upper() for x in fruits]
newfruits = [x if x !="bananans" else "oranges" for x in fruits]
print(newfruits)