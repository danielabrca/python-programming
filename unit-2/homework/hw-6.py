#list of the Marvel movies
marvel_movies = ['Captain America: The First Avenger', 'Iron Man', 'Guardians of The Galaxy', 'The Incredible Hulk',
                 'The Avengers', 'Ant-Man', 'Spider-Man: Homecoming', 'Doctor Strange', 'Black Panther',
                 'Avengers: Infinity War', 'Captain Marvel', 'Thor: The Dark World', 'The Amazing Spider-Man']

#Marvel movies that contain word "The"
special_marvel_movies = []

#iterating each movie in marvel_movies
for idx in marvel_movies:
    #checking condition
    if 'the ' in idx:
        special_marvel_movies.append(idx)

print(special_marvel_movies)