def add(*args):
    total = 0
    for item in args:
        total += item

    return total

print(add(1,2,3,4,5,6,7,8,9,10))

def sum_pairs(my_list, total):
    first = 0
    second = 1
    while first != second:
        a = my_list[first]
        b = my_list[second]
        if a + b == total:
            return [a, b]
        if second < len(my_list) - 1:
            second += 1
        else:
            first += 1
    
    return [None, None]

print(sum_pairs([7, 5, 2, 8, 2, 5], 10))
