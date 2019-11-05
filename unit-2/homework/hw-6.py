#list of the Marvel movies (if the list is too long, don't tab when break the list in more rows)
marvel_movies = ['Captain America: The First Avenger', 'Iron Man', 'Guardians of The Galaxy', 'The Incredible Hulk',
'The Avengers', 'Ant-Man', 'Spider-Man: Homecoming', 'Doctor Strange', 'Black Panther',
'Avengers: Infinity War', 'Captain Marvel', 'Thor: The Dark World', 'The Amazing Spider-Man']

#Marvel movies that contain word "The"
special_marvel_movies = []

#iterating each movie in marvel_movies
for movie in marvel_movies:
    #checking condition
    if 'the ' in movie.lower():
        special_marvel_movies.append(movie)

print(special_marvel_movies)

#Study difference between FUNCTION and METHOD!!!