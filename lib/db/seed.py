#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///migrations_test.db')
    Session = sessionmaker(bind=engine)
    session = Session()

session.query(Artist).delete()
session.commit()

a1 = Artist(name="Mac Miller")
a2 = Artist(name="Ludwig van Beethoven")

# l1 = Listener(name="Jesse")
# l2 = Listener(name="Andre")
# l3 = Listener(name="Tom")
# l4 = Listener(name="Collin")

# s1 = Song(name="Ladders", artist_id= a2, listener_id= l1)
# s2 = Song(name="Für Elise", artist_id= a1, listener_id= l4)

session.add_all([a1, a2])
session.commit()