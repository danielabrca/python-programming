countries = ['Mexico', 'Mexico', 'Jamaica', 'Tahita', 'USA', 'Thailand', 'Greece', 'Philippines', 'Puerto Rico', 'Jamaica']
destinations = ['Cozumel', 'Cancum', 'Montego Bay', 'Bora Bora', 'Maui', 'Phuket', 'Mykonos', 'Palawan', 'Vieques', 'Negril']

for idx in range(len(destinations)):
    destinations[idx] += ' - ' + countries[idx]

print(destinations)