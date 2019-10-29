worker_type = 'part_time'
hours_worked = 27

weekly_wage = 0
if worker_type == 'full_time':
    weekly_wage = (40 * 50) + ((hours_worked - 40) * 60)
elif worker_type == 'part_time':
    weekly_wage = (20 * 65) + ((hours_worked - 20) * 70)
else:
    weekly_wage = hours_worked * 120 * 0.75
print(weekly_wage)