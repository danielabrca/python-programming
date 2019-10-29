#calculate the sum of all the even numbersbetween 1000, and 10,000.
sum_even = 0
for i in range(1000, 10001, 2):
    sum_even = sum_even + i
print (f'The sum of even numbers between 1000 and 10,000 is: {sum_even}')