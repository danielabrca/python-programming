def reverse_list(my_list):
    result = []
    idx = len(my_list) - 1
    while idx >= 0:
        result.append(my_list[idx])
        idx -= 1
    
    return result

#calling reverse_string
'''
print(reverse_list([1,2,3,4,5]))

new_list = reverse_list(['a','b','c','d','e'])

print(new_list)

classmates = ['emma', 'chizea', 'daniela']

print(reverse_list(classmates))
'''

def encode_string(string):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    result = ''
    for character in string:
        for idx in range(len(letters)):
            if character == letters[idx]:
                result += str(idx + 1)
                
    return result

#print(encode_string('happy'))

def pivot_split(my_list, my_num):
    left = []
    right = []
    for num in my_list:
        if num < my_num:
            left.append(num)
        else:
            right.append(num)
    
    return [left, right]

print(pivot_split([12,7,8,15,3,9,11,-7], 8))
