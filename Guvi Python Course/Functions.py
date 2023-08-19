def trialfunction(x,y):
    print(x + "  "+y)

trialfunction("Black","Bear")

list = ['bike','bus','scooter','cycle']

def type(p):
    print(p*3)

# Function As Paremeter
def crazy_loop(crazy,list):
    for items in list:
        crazy(items)

crazy_loop(type,list)
