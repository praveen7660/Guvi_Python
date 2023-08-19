# serialization and deserialization
# used to create list tuple or anything into bytes i.e [0,1]
#
# Pickling is Taking 2D data and converting it into 1D and deserialization too that is => taking 1D converting it into 2D

import pickle

mydict = {'1':'a','2':'b'}

# wb => write byte mode
pickle_file = open("picklefile.txt","wb")
pickle.dump(mydict, pickle_file)

# rb => read byte mode
pickle_file = open("picklefile.txt","rb")
new_dict = pickle.load(pickle_file)

print(new_dict)