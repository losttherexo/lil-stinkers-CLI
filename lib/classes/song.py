from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Song, Stream
import webbrowser


engine = create_engine('sqlite:///db/playlist.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_song(self):
    print(' ')
    name = input('Song name: ')
    artist = input('Artist: ')
    year = input('Year released (can be left blank): ')
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
        stream = session.query(Stream).filter(Stream.song_name == song)


        stream.delete()
        session.delete(removed_song)
        session.commit()

        print(f"{removed_song.name} by {removed_song.artist} was removed!")
    else:
        print(' ')
        print('Uh-oh! This input is case sensitive!')
        print(' ')
        choice = input('Try again? (Y/N): ')
        if choice.lower() == 'y':
            remove_song(self)
        else:
            pass

def search_song(self):
    print(' ')
    query = input('Song: ') 
    found_song = False
    for s in self.songs:
        if s.name.lower() == query.lower():
            print(' ')
            print(f'{s}')
            found_song = True
            print(' ')
            choice = input("Would you like to 'play' this song? ")
            if choice == 'play':
                webbrowser.get(using='chrome').open_new(s.yt_link)
    if not found_song:
        print('\nSong not found :c')

def search_artist(self):
    print(' ')
    query = input('Artist: ')
    queried_artist = ''
    found_artist = False
    song_list = []
    for s in session.query(Song):
        if s.artist.lower() == query.lower():
            song_list.append(s)
            queried_artist = s.artist
            found_artist = True
    if found_artist:
        print(' ')
        print(f'Songs by {queried_artist}:')
        print(' ')
        for index, song in enumerate([s for s in song_list]):
            print(f'{index + 1}. {song.name} by {song.artist} ')

    if not found_artist:
        print('\nArtist is not in Database :c')

def songs(self):
    for index, song in enumerate([s for s in session.query(Song)]):
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
    print(' ')
    name = input('Song: ')
    query = session.query(Song).filter(Song.name == name)
    song = query.first()
    songs_list = [s.song for s in session.query(Stream) if s.song == song]
    song_count = len(songs_list)
    print(' ')
    if song_count == 1:
        print(f"{song.name} by {song.artist} was played {song_count} time!")
    elif song_count > 1:
        print(f"{song.name} by {song.artist} was played {song_count} times!")
    else:
        print('Looks like you made a typo, try again!')