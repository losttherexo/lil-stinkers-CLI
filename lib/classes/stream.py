from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Stream, Song
from classes.song import *
import webbrowser

engine = create_engine('sqlite:///db/playlist.db')
Session = sessionmaker(bind=engine)
session = Session()

def stream_history(self):
    for index, stream in enumerate(self.streams):
        print(f'{index + 1}. {stream.listener.name} recently played {stream.song.name} by {stream.song.artist}')

def add_stream(self):
    print('')
    song = input("Song: ")

    if song in [s.name for s in self.songs]:
        query = session.query(Song).filter(Song.name == song)
        song_inst = query.first()
        queue = Stream(song_name = song, song = song_inst, listener = self.user)
        session.add(queue)
        session.commit()

        webbrowser.get(using='chrome').open_new(song_inst.yt_link)
    else:
        print(' ')
        print('You gotta upload the song first!')
        add_song(self)