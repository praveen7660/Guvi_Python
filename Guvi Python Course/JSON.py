'''
JASON => JavaScript object Notation

it is commonly used to transmit and receive data between server and web aplication in JSON format

parse => One string of data into different type
like => take html -> convert to more readable format
'''

'''
all the Objects of python and there equivalent conversion to Json can only occur only if they are :-

dict
list
tuple
string
int
float
boolean
None

only this can be converted to json
'''

import json

'''
# Jason to Dictionary
person = '{"name":"Bob","Language":["English","French"]}'

person_dict = json.loads(person)
print(person_dict)

print(person_dict['Language'])



# How to parse a Json File into python
# json.loads gives us a dictionary
with open("data.json") as f:
    data = json.load(f)

print(data)


# dictionary => Json
person = {"name":"Bob","age":12,"languages":"English"}

person_json = json.dumps(person)

print(person_json)


# convert dictionary to jason and save in person.txt
person = {"name":"Bob","age":12,"languages":"English"}


with open ('person.txt','w') as json_file:
    json.dump(person,json_file)


# Print the json data in more Readable Format
with open("data.json") as f:
    data = json.load(f)
#  Indent => for spaces
# sort_keys => sort in ascending order
print(json.dumps(data, indent =4,sort_keys = True))

'''