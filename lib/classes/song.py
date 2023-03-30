from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Song

engine = create_engine('sqlite:///db/playlist.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_song(self):
    print(' ')
    name = input('Name: ')
    artist = input('Artist: ')
    year = input('Year Released (can be left blank): ')
    new_song = Song(name = name, artist = artist, year = year)
    print(' ')

    session.add(new_song)
    session.commit()

    print(f'{name} by {artist}, was added to our playlist!')
    self.songs.append(new_song)

def songs(songs):
    for index, song in enumerate(songs):
        print(f'{index + 1}. {song.name} by {song.artist}')