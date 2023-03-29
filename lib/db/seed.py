#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///migrations_test.db')
    Session = sessionmaker(bind=engine)
    session = Session()

session.query(Artist).delete()
session.query(Listener).delete()
session.query(Song).delete()
session.commit()

#artist = name, genre, founded
a1 = Artist(name="Mac Miller", genre= "Rap", founded=2010)
a2 = Artist(name="Ludwig van Beethoven", founded=1782)

# listener = name, age
l1 = Listener(name="Jesse", age = 30)
l2 = Listener(name="Andre", age = 27)
l3 = Listener(name="Tom", age = 28)
l4 = Listener(name="Collin", age = 23)

# song: name, year, stream_count, artist, listener (stretch:link)

s1 = Song(name="Ladders", year=2018, stream_count=100, artist= a2, listener= l1)
s2 = Song(name="Für Elise", year=1810, stream_count=101, artist= a1, listener= l4)

session.add_all([a1, a2, l1, l2, l3, l4, s1, s2])
session.commit()