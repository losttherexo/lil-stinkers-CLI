#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///playlist.db')
    Session = sessionmaker(bind=engine)
    session = Session()

# session.query(Stream).delete()  -- don't uncomment and run this file unless u want to delete our DB
session.query(Listener).delete()
# session.query(Song).delete() -- don't uncomment and run this file unless u want to delete our DB
session.commit()

s1 = Song(name='Mirrors', artist="lost,there", year=2021, yt_link= "https://www.youtube.com/watch?v=Bo_XvrwLPIk")
s2 = Song(name="Robbers", artist="The 1975", year=2013, yt_link= "https://www.youtube.com/watch?v=wjHgiSx0RNQ")

l1 = Listener(name="Jesse", age= 30)
l2 = Listener(name="André", age= 27)
l3 = Listener(name="Tom", age= 28)
l4 = Listener(name="Collin", age= 23)

st1 = Stream(song_name=s1.name, song=s1, listener=l4)
st2 = Stream(song_name=s2.name, song=s2, listener=l3)
st3 = Stream(song_name=s1.name, song=s1, listener=l1)
st4 = Stream(song_name=s1.name, song=s1, listener=l2)
st5 = Stream(song_name=s2.name, song=s2, listener=l4)
st6 = Stream(song_name=s1.name, song=s2, listener=l3)
st7 = Stream(song_name=s1.name, song=s1, listener=l2)
st8 = Stream(song_name=s2.name, song=s2, listener=l1)


session.add_all([s1, s2, st1, st2, st3, st4, st5,st6,st7,st8])
session.commit()