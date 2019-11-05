#list of temperatures
temperature_readings = [25, 18, -5, 11, -3, -15,  8, -18, 6, 13]

#sum of positive numbers and sum of and negative numbers in the list
pos_sum, neg_sum = 0, 0

#count of positive numbers and count of negative numbers in the list
pos_count, neg_count = 0, 0

#average of positive numbers and average of negative numbers in the list
pos_mean, neg_mean = 0, 0

#iterating each temperature in temperature_readings
for temperature in temperature_readings:
    #checking condition
    if temperature >= 0:
        pos_sum += temperature
        pos_count += 1
        pos_mean = pos_sum / pos_count
    else:
        neg_sum += temperature
        neg_count += 1
        neg_mean = neg_sum / neg_count

print('Average of positive readings:', round(pos_mean, 1), 'degrees')
print('Average of negative readings:', round(neg_mean, 1), 'degrees')

#colocar o calculo da media dentro do print, dentro do round