from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Song

engine = create_engine('sqlite:///db/migrations_test.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_song(self):
    print('')
    print_artists(self.artists)
    print_listeners(self.listeners)

def print_artists(artists):
    print([a for a in artists])
    print(' ')

def print_listeners(listeners):
    print([l for l in listeners])
    print(' ')