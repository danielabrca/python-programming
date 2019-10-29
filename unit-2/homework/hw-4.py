string = 'Python Programming at General Assembly is Awesome!!'
#strings is imutable!!!

new_string = ''
for a in string:
    if a != ' ' and a != 's' and a != 'm':
        new_string += a

print(new_string)