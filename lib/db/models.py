class Artist:
    
    all_artists = []

    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        Artist.all_artists.append(self)

class Listener:

    all_listeners = []

    def __init__(self, name,):
        self.name = name
        Listener.all_listeners.append(self)

class Song:

    all_songs = []

    def __init__(self, name, artist_instance, listener_instance):
        self.name = name
        self.artist = artist_instance
        self.listeners = listener_instance
        Song.all_songs.append(self)
