#function to add two integers
def add(num1, num2): #function definition, it would not execute until the function is called
    return num1 + num2

#when you define a function, what you have inside the brackets is the parameters
#when you call a function, what you have inside the brackets is the arguments

#ways to call a function:
print(add(5, 10)) #pass to print function
result = add(50, 20) #assign to a variable

#function with no argument
#function to display hello there
def say_hello():
    print('Hello There!')

say_hello()

#function that returns the lenght of a string
def lenght(string):
    return len(string)

print(lenght('What a wonderful world'))

#function to return the sum of integers in a list
def sum_int(a_list):
    result = 0
    if type(a_list) is list:
        for num in a_list:
            if type(num) is int:
                result += num
    else:
        print('invalid argument')
        return    
    return result

'''
#function to reverse a string
def daniela_reverse(string):
    result = ''
    for character in string: 
        result = character + result
    return result

string = 'Test as daniela'

print(daniela_reverse(string))
'''

#different way
def daniela_reverse(string):
    result = ''
    lenght = len(string) - 1
    while lenght >= 0:
        result = result + string[lenght]
        lenght = lenght - 1
    return result

string = 'Daniela'

print(daniela_reverse(string))

