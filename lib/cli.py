#!/usr/bin/env python3

from db.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CLI:
    def __init__(self, user_input):
        self.artists = [artist for artist in session.query(Artist)]
        self.listeners = [listener for listener in session.query(Listener)]
        self.songs = [song for song in session.query(Song)]
        self.name = user_input
        self.start()
    
    def start(self):
        print(' ')
        print(f"Welcome the Little Stinker's Playlist {self.name}!")
        print(' ')

        exit = False
        while exit == False:
                choice = input(f"Enter 'list' to see all Artists, Songs, or" 
                + " Listeners, 'search' to search for a specific artist, song" 
                + " or listener, or 'add' to add a song to our cohort's"
                + " playlist!")
                print(' ') 
                if choice.lower() == "list":
                    show_lists(self)
                elif choice.lower() == "search":
                    print('ugh ur fake')
                elif choice.lower() == 'add':
                     pass
                elif choice.lower() == 'help':
                     pass

                user_input = input("Would you like to turn off the sound ? (Type Y/N): ")
                print(' ')
                if user_input.lower() == 'y':
                    print('Goodbye friend!')
                    print(' ')
                    exit = True

def show_lists(self):
    user_action = input("Would you like to see the artists, songs, or listeners?")
    if user_action.lower() == 'artists':
        print(' ')
        artists(self.artists)

def artists(artists):
    print([a for a in artists])
    print(' ')

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/migrations_test.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Your Name: ")
    CLI(user_input)