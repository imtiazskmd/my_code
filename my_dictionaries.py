# Dictionaries cannot be sorted because these are mapping not sequence
# Use dict when you need a logical association between key and value pair.
# It helps in fast lookup for your data based on a custom key.
# Use when your data is being constantly modified.

mydict={'apple':20, 'orange':5, 'pomegranate':10, 'mylist':[1,2,3], 'dict':{'inside': 8}}
print(f'Price of orange is {mydict['orange']}')  # I am getting the value by calling the key name

#let us call mylist key which has list elements
print(mydict['mylist'])

#let us call the inside key in dict key
print(mydict['dict']['inside'])

# let us add a new key to this dictionary
mydict['banana']=3
print(mydict)

# let us call all the keys, values and items one after the another
print(f'Printing all keys: {mydict.keys()}')
print(f'Printing all values: {mydict.values()}')
print(f'printing all the items: {mydict.items()}')

# few tricky questions & how to call them
# print 'hello' from the below dictionary
d={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1])   # this dictionary is a combination of dictionary & list, hence we are using key name and index value of list to select the appropriate element

# print 'hi' from the below dictionary
d={'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hi']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2])



