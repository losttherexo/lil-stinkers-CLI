#!/usr/bin/env python3

from db.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes.stream import *
from classes.listener import *
from classes.song import *

class CLI:
    def __init__(self, user):
        self.songs = [song for song in session.query(Song)]
        self.listeners = [listener for listener in session.query(Listener)]
        self.streams = [stream for stream in session.query(Stream)]
        self.name = user.name
        self.user = user
        session.expunge(user)
        self.start()

    def start(self):
        print(' ')
        print(f"Welcome the Little Stinker's Playlist {self.name}!")
        print(' ')

        exit = False
        while exit == False:
                choice = input(f"Enter 'list' to see a list of all our" 
                + " songs or recent history, 'search' to find a specific" 
                + " artist or song, or 'add' to add a song to our"
                + " playlist! ")
                print(' ') 
                if choice.lower() == 'list':
                    show_lists(self)
                elif choice.lower() == 'search':
                    search_data(self)
                elif choice.lower() == 'add':
                    add_data(self)
                elif choice.lower() == 'help':
                    display_help()

                print(' ')
                user_input = input("Would you like to turn off the sound? (Type Y/N): ")
                print(' ')
                if user_input.lower() == 'y':
                    print('Goodbye friend!')
                    print(' ')
                    exit = True

def show_lists(self):
    user_action = input("Would you like to to check out our 'songs' list or recent 'history'? (Choose one): ")
    if user_action.lower() == 'songs':
        print(' ')
        songs(self)
    elif user_action.lower() == 'history':
        print(' ')
        stream_history(self)

def search_data(self):
    new_data = input("Would you like to search for a 'song' or an 'artist'? ")
    if new_data.lower() == 'song':
        search_song(self)
    elif new_data.lower() == 'artist':
        search_artist(self)

def add_data(self):
    new_data = input("Would you like to 'queue' a song or"
    + " 'upload' a new song if not yet in our playlist? ")
    if new_data.lower() == 'upload':
        add_song(self)
    elif new_data.lower() == 'queue':
        add_stream(self)

def display_help():
    print("If you've made it this far you are clearly extremely curious or"
    + " just wanna try to break our code so here's some pointers to avoid"
    + " doing that!")
    print(" ")
    print("Look for words wrapped in 'single quotes' and they'll take you" 
    + " to some sort of musical or administrative wonderland! glhf ")

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/playlist.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    print(' ')
    print("There's always an afterparty...")
    print('')
    try:
        user = input("Name? ")
        if user in [l.name for l in session.query(Listener)]:
            test = [l for l in session.query(Listener) if l.name == user]
            CLI(test[0])
        elif user.lower() == 'kevin':
            print('')
            print('ERROR: No stinkers allowed ;P')
            print('')
        else:
            age = input('Age: ')
            new_user = Listener(name = user, age = age)
            session.add(new_user)
            session.commit()      
            CLI(new_user)
    except KeyboardInterrupt:
        print('\n\nSee ya later pal!\n')
