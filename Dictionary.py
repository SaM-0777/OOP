##Dict is an unordered set or collection of items or objects where unique keys are mapped yhe values
##These keys are used to access the corresponding paired value. While the keys are unique, values can be common and repeated
##The data type of a value is also mutable and can change whereas, the data type of keys must be mutable such as strings, numbers or tuples


##Example 1
d = {'cat' : 'cute', 'dog' : 'furry'}
print(d['cat'])
print('cat' in d)   ##Print True

d['fish'] = 'wet'   ##Set an Entry in a Dict
print(d['fish'])
print(d)

print(d.get('monkey', 'N/A'))   ##Get an Element with default; prints "N/A"
print(d.get('fish', 'N/A'))     ##Get an Element with default; prints "N/A"

del d['fish']                   ##Remove an Element from Dict
print(d.get('fish', 'N/A'))     ##If fish is not in dict it will print "N/A"
print(d)

###Changing existing value
dict_list = {'name' : 'Rama', 'hobbies' : ['painting', 'singing', 'cooking']}

dict_list['name'] = 'krishna'
print("Name : ", dict_list['name'])

##Adding new Key:value
dict_list = {'name' : 'Ariel', 'hobbies' : ['painting', 'singing', 'cooking']}

dict_list['age'] = 11
print("Dict : ", dict_list)

##Deleting a key:value
del dict_list['name']
print(dict_list)

print("Hobbies : ", end = '')
for i in dict_list['hobbies']:
    print(i, end = ', ')

##Predefined Dict Func
#clear(), copy(), get(), items(), fromkeys(), keys(), update(), pop(), values(), popitems()

##How Dict is diff from list ?
# A dict is a composite datatype in python which resembles a list
# List has an ordered set of objects which can iterate and can be referenced and accessed by an index number unlike a dict which is unordered and
# has a key:value pair where values are accessed by keys