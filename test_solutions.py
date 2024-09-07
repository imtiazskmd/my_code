# Use range() to print all the even numbers from 0 to 10.

print('Printing even numbers from the range:')
for num in range(0,11,2):
    print(num)

#Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

print('\nUsing list comprehension to print num dividend by 3:')
s_list=[s for s in range(1,50) if s%3==0]
print(s_list)

#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
print('\nUsing split() method to find the even word:')
for word in st.split():
    if len(word)%2==0:
        print('This word is even:',word)   # We can also add else statement below to print odd word when the if statement is false

# Write a program that prints the integers from 1 to 20. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

print('\nPrinting Fizz,Buzz,Fizzbuzz based on divisble condition:')
for num in range(0,21):
    if num%3==0 and num%5==0:
        print('FizzBuzz')
    elif num%3==0:
        print('Fizz')
    elif num%5==0:
        print('Buzz')

#Use a List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
print('\nCreating a list with first letters of every word in a string:')
c_list=[word[0] for word in st.split()]    # selecting index[0] from each word in the string by using split()
print(c_list)
