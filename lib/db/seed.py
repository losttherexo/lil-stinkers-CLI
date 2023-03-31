#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///playlist.db')
    Session = sessionmaker(bind=engine)
    session = Session()

# session.query(Stream).delete()
# session.query(Listener).delete()
# session.query(Song).delete()
# session.commit()

# s1 = Song(name='Ladders', artist="Mac Miller", year=2018, yt_link= "https://www.youtube.com/watch?v=0gzmFo8UiJQ&list=RD0gzmFo8UiJQ&start_radio=1")
# s2 = Song(name='Hollywood Baby', artist="100 Gecs", year=2023, yt_link="https://www.youtube.com/watch?v=UtfkrGRK8wA")

# l1 = Listener(name="Jesse", age= 30)
# l2 = Listener(name="Andre", age= 27)
# l3 = Listener(name="Tom", age= 28)
# l4 = Listener(name="Collin", age= 23)

st1 = Stream(song_name=s1.name, song=s1, listener=l4)
st2 = Stream(song_name=s2.name, song=s2, listener=l3)
st3 = Stream(song_name=s3.name, song=s3, listener=l1)
st4 = Stream(song_name=s3.name, song=s3, listener=l2)
st5 = Stream(song_name=s4.name, song=s4, listener=l1)
st5 = Stream(song_name=s2.name, song=s2, listener=l1)


session.add_all([st1, st2, st3, st4, st5, st6])
session.commit()