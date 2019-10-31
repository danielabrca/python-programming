cohort_4 = ['Daniela', 'Keerthi', 'Sahil', 'Shilaj', 'Kyle', 'Emma', 'Julian', 'Chizea', 'Christina', 'Lizhi', 'Allaina']

print(len(cohort_4))

#access items in list using position (index)

print(cohort_4[0]) #print first item in list

print(cohort_4)

#add items to the list, use append

cohort_4.append('Princeton')
print(cohort_4)

cohort_4.remove('Julian')
print(cohort_4)

#create a new list with only the floats
values = [2.3, 45, 11, -5, 3.5, 7.9, 11.7, 40, 85.6, 77.1]
float_value = []
for value in values:
    if type(value) is float:
        float_value.append(value)
print(float_value)

#find the average of each list, store in a new list
weights = [[50, 25, 75], [95.7, 38.3, 55.2], [88, 45, 16]]
averages = []

for weight in weights:
    list_sum = 0
    for value in weight:
        list_sum += value
    averages.append(list_sum/len(weight))

print(averages)

for row in range(1, 11):
    for col in range(1, row + 1):
        print('*', end=' ')
    print()

'''
for i in range(11):
    print('*' * (i+1))
'''

#using indexes to access list items
#use index if we need to edit items in list

#set all the negative readings to 0
readings = [3.5, -7.7, -9.8, 13.6, 22.5, 19.7, -8.6]

for idx in range(len(readings)):
    if readings[idx] < 0:
        readings[idx] = 0

print(readings)

#find the position of an item in a list
current_age = 25
ages = [15, 17, 27, 35, 12, 25, 55, 40, 31, 20]

for idx in range(len(ages)):#position start in 0 position and goes to the size of the list - 1 / The position is not the ITEM/ELEMENT!!! 
    if ages[idx] == current_age:
        print('current_age is found at position', idx)


