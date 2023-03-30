from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Song
import webbrowser
from collections import Counter
engine = create_engine('sqlite:///db/playlist.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_song(self):
    print(' ')
    name = input('Song name: ')
    artist = input('Artist: ')
    year = input('Year Released (can be left blank): ')
    link = input('Youtube link: ')
    new_song = Song(name = name, artist = artist, year = year, yt_link = link)
    print(' ')

    session.add(new_song)
    session.commit()

    print(f'{name} by {artist}, was added to our playlist!')
    self.songs.append(new_song)
    print('')
    print("Don't forget to queue it up now ;)")



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

def search_song(self):
    print(' ')
    query = input('Insert Song Name:') 
    found_song = False
    for s in self.songs:
        if s.name.lower() == query.lower():
            print(' ')
            print(f'{s}')
            found_song = True
            choice = input("Would you like to 'play' this song?")
            if choice == 'play':
                print(s.yt_link)
                webbrowser.get(using='chrome').open_new(s.yt_link)
    if not found_song:
        print('\nSong is not in Database :c')



def songs(self):
    for index, song in enumerate(self.songs):
        print(f'{index + 1}. {song.name} by {song.artist}')
    
    print(' ')
    choice = input("Would you like to 'add', 'remove', or 'count' the streams of a song? ")
    if choice.lower() == 'add':
        add_song(self)
    elif choice.lower() == 'remove':
        remove_song(self)
    elif choice.lower() == 'count':
        stream_count(self)

    
def stream_count(self):
    name = input('song name: ')
    query = session.query(Song).filter(Song.name == name)
    song = query.first()
    songs_list = [s.song for s in session.query(Stream) if s.song == song]
    print(Counter(songs_list).most_common(1)[0][1])
