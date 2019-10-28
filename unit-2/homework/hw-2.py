worker_type = 'full_time'
hours_worked = 45

if worker_type == 'full_time':
    value_per_hour = 50
    overtime_per_hour = 60
    weekly_limit = 40
    tax = 0
elif worker_type == 'part_time':
    value_per_hour = 65
    overtime_per_hour = 70
    weekly_limit = 20
    tax = 0
elif worker_type == 'contractor':
    value_per_hour = 120
    overtime_per_hour = 0
    weekly_limit = 0
    tax = 25

if weekly_limit > 0 and hours_worked > weekly_limit:
    overtime = hours_worked - weekly_limit
    hours_worked = weekly_limit
    
weekly_wage = (hours_worked * value_per_hour) + (overtime * overtime_per_hour)
print(weekly_wage)