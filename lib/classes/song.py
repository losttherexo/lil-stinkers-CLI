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

def remove_song(self):
    print(' ')
    song = input('What song would you like to remove? ')

    if song.lower() in [s.name.lower() for s in self.songs]:
        print(' ')
        query = session.query(Song).filter(Song.name == song)
        removed_song = query.first()
        
        session.delete(removed_song)
        session.commit()
    else:
        print(' ')
        print('This input is case sensitive, try again! :)')
        
        remove_song(self)
    

def songs(self):
    for index, song in enumerate(self.songs):
        print(f'{index + 1}. {song.name} by {song.artist}')
    
    print(' ')
    choice = input("Would you like to 'add' or 'remove' a song? ")
    if choice.lower() == 'add':
        add_song(self)
    elif choice.lower() == 'remove':
        remove_song(self)