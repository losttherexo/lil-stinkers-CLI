from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Stream

engine = create_engine('sqlite:///db/playlist.db')
Session = sessionmaker(bind=engine)
session = Session()

def stream_history(self):
    for index, stream in enumerate(self.streams):
        print(f'{index + 1}. {stream.song_name} recently played {stream.song_id} by {stream.song_id}!')