from db.artist import Artist
from db.listener import Listener

class Song:

    all_songs = []

    def __init__(self, name, artist_instance, listener_instance):
        self.name = name
        self.artist = artist_instance
        self.listeners = listener_instance
        Song.all_songs.append(self)