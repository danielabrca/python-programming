#the for loop
'''
name ='Princeton'
for count in range(1, 11):
    print(name)


#print the odd numbers between 1 and 10
for num in range(1, 11):
    if num % 2 == 1:
        print(num)

'''
#print the sum of the even numbers
total = 0
for num in range(1, 11):
    if num % 2 == 0:
        total += num


#store your full name in a variable
#loop over your name
#if you find a vowel, print it
#'a', 'e', 'i', 'o', 'u' - vowels

name = 'Princeton Ebanks'
#for each letter in my name
for letter in name:
    #if the letter is a vowel, print it
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        print(letter)


