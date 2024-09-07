mystring='Hello World'

#using start & stop together
print(mystring[1:5:])

#using step
print(mystring[::2])

#reversing the string
print(mystring[::-1])

#Strings are immutable but we can concatenate it. Using upper & concatenation
newstring=mystring[:5:]
print(newstring.upper()+ ' John')

#Using split method in string by using print formatting
print('Example of {} {}'.format ('split',mystring.split()))

#Using f-string
print(f'{newstring}, This is an example of f-string')

#Another example of f-string
name,age ='John',5     # I observed that we can assign string & int in this way too
print(f'{name} is {age} years old')


