'''
#1 - reversing a list without create a copy of it
my_list = [1, 2, 3, 4, 5]
#call the method .reverse()
my_list.reverse()
print(my_list)

#2 - reversing a list creating a copy of it slicing the list
my_list = [1, 2, 3, 4, 5] 
reversed_list = my_list[::-1]
print(reversed_list)

#3 - reversing a list using the builtin reversed function, it will neither reverse the list in place (option 1)nor it will create a copy (option 2)
my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
'''

#4 - in this function we are starting at the last element in my_list and appending it as the first element
# in result, the list that will show the reversal. 
def reverse_list(my_list):
    new_list = []
    lenght = len(my_list) - 1
    while lenght >= 0:
        new_list.append(my_list[lenght])
        lenght -= 1
    return new_list

print(reverse_list([1, 2, 3, 4, 5]))