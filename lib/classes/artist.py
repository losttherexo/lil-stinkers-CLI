from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Artist

engine = create_engine('sqlite:///db/migrations_test.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_artist(self):
    artist_names = [a.name for a in self.artists]
    print('')
    artist_input = input('Enter artist name: ')

    if artist_input in artist_names:
        print(' ')
        print('artist already in db')
    else:
        genre = input('Artist genre: ')
        founded = input('Year they got started (if unknown, leave blank c:): ')
        new_artist = Artist(name = artist_input, genre = genre, founded = founded)

        session.add(new_artist)
        session.commit()

        self.artists.append(new_artist)
