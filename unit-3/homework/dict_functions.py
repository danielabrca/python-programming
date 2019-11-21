#Problem 1: Write a function called frequency_counterthat accepts a string, and returns a dictionary
#with the number of times each character occurs in the string
#For example:frequency_counter('happy')should return{'h': 1,'a': 1,'p': 2,'y': 1}

def frequency_counter(string):
#    string = string.lower()
    lcDict = {}
    for l in string:
        if l in lcDict:
            lcDict[l] +=1
        else:
            lcDict[l]= 1
    print(lcDict)

frequency_counter('Daniela Andrade')


#Problem 2: Write a function called list_to_dict that accepts a person list (which is a list of lists),
#and returns a dictionary. Each list in the person list has only two items. The keys of your
#result dictionary should be the first item in each list, and the value should be the second item.
#For example:list_to_dict([['name','Alice'], ['job','Engineer'],['city','Toronto']])
#should return{'name':'Alice','job':'Engineer','city':'Toronto'}

def list_to_dict(people):
    result = {}
    for item in people:
        result[item[0]] = item[1]

    return result

persons = [['name', 'Alice'], ['job', 'Engineer'], ['city', 'Toronto']]

print(list_to_dict(persons))