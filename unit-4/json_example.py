import json
#properly formatted json
#keys enclosed in double quotation
#enclosed with curly braces, square brackets can be used
with open('cohort_4.json', 'r') as cohort_file:
    cohort = json.load(cohort_file) #converts json file to python dictionary

print(type(cohort))
print(json.dumps(cohort, indent=2))
#print(cohort)