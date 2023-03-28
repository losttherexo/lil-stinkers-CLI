#!/usr/bin/env python3

from db.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CLI:
    def __init__(self, user_input):
        # self.artists = [artist for artist in session.query(Artist)]
        # self.listeners = [listener for winery in session.query(Winery)]
        # self.bottles = [bottle for bottle in session.query(Bottle)]
        self.name = user_input
        self.start()
    
    def start(self):
        print(' ')
        print(f"Welcome The Little Stinker's Playlist {self.name}!")
        print(' ')

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/migrations_test.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Your Name: ")
    CLI(user_input)