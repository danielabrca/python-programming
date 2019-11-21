#create a playlist class. The paylist has a name and a list of track
#each track is a dictionary, with title, artist, length of track

#Write methods to add a track, to remove a track, to shuffle the playlist

track_file_name = 'tracks.json'

class Playlist:
    def __init__(self, n):
        self.name = n
        self.tracks = []

    def add_track(self, title, genre, artist, year, length):
        track = {}
        track['title'] = title
        track['genre'] = genre
        track['artist'] = artist
        track['year'] = year
        track['length'] = length
        self.tracks.append(track)

    def remove_track(self, title):
        for idx in range(len(self.tracks)):
            if title == self.tracks[idx]['title']:
                break
        self.tracks.pop(idx)
    
    def save_tracks(self):
        #open file for writing
        with open(track_file_name, 'w') as track_file:
            #for track in self.tracks:
            #    track_file.write(json.dumps(track))
                track_file.write(json.dumps(self.tracks))
    
    def load_tracks(self):
        #load the data from the tracks.txt file
        with open(track_file_name, 'r') as track_file:
            data = json.load(track_file)
        #set the class tracks variable to the data loaded in
        self.tracks = data
        #pass

'''
pl = Playlist('tunes')
pl.add_track('title': 'Put Your Records On','genre': 'Soul', 'artist': 'Corinne Bailey', 'year': '2006','length': 3.34)
pl.add_track('title': 'Like A Star', 'genre': 'Soul', 'artist': 'Corinne Bailey', 'year': '2005', 'length': 4.03)
pl.add_track('title': 'Another Love', 'genre': 'Pop', 'artist': 'Tom Odell', 'year': '2012', 'length': 4.05)
pl.add_track('title': 'Thinking Out Loud', 'genre': 'Pop', 'artist': 'Ed Sheeran', 'year': '2014', 'length': 4.42)
pl.add_track('title': 'Gravity', 'genre': 'Pop', 'artist': 'John Mayer', 'year': '2006', 'length': 4.06)
pl.add_track('title': 'Budapest', 'genre': 'Funk', 'artist': 'George Ezra', 'year': '2014', 'length': 3.21)
pl.add_track('title': 'Take Me To Church', 'genre': 'Rock', 'artist': 'Hozier', 'year': '2016', 'length': 4.02)
pl.add_track('title': 'Ho Hey', 'genre': 'Folk', 'artist': 'The Lumineers', 'year': '2011', 'length': 2.41)
pl.add_track('title': 'Let Her Go', 'genre': 'Pop', 'artist': 'Passenger', 'year': '2013', 'length': 4.13})
pl.add_track('title': 'Summertime Sadness', 'genre': 'Pop', 'artist': 'Lana Del Rey', 'year': '2012', 'length': 4.25)
pl.add_track('title': 'Smile', 'genre': 'Hip Hop', 'artist': 'Lily Allen', 'year': '2006', 'length': 3.17)
'''

new_playlist = Playlist('new music')
#pl.save_tracks()
new_playlist.load_tracks()
print(new_playlist.tracks)
