#while loop is executed only when a condition is met
import random #random number module

'''
val = 1
while val < 10:
    print(val)
    val +=1 #increment val

#print val (1) plus 1 until result (val) is less than 10 (< 10)
'''
'''
#guessing game

#all keyboar input is string
#correct_answer = 7
correct_answer = random.randint(1, 10)
guess = int(input('guess my number (1 - 10): '))

while guess != correct_answer:
    guess = int(input('Wrong. Try again!'))

print('You are correct!!!')
'''
#how do you break a loop?

names = ['jake', 'jill', 'mary', 'jane', 'kate']

idx = 0
while idx < len(names):
    if 'mary' == names[idx]:
        print('Found Mary!!')
        break
    idx += 1

#how do we loop forever:
while True:
    answer = input('continue(y/n)' )
    if answer == 'n':
        break