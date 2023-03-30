#!/usr/bin/env python3

from db.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes.stream import *
from classes.listener import *
from classes.song import *

class CLI:
    def __init__(self, user_input):
        self.songs = [song for song in session.query(Song)]
        self.listeners = [listener for listener in session.query(Listener)]
        self.streams = [stream for stream in session.query(Stream)]
        self.name = user_input
        self.start()
    
    def start(self):
        print(' ')
        print(f"Welcome the Little Stinker's Playlist {self.name}!")
        print(' ')

        exit = False
        while exit == False:
                choice = input(f"Enter 'list' to see a list of all our" 
                + " songs, 'search' to find a specific artist," 
                + " song, or listener, or 'add' to add a song to our"
                + " playlist's queue! ")
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
    user_action = input("Would you like to to check out our 'songs' list or recent 'history'? (Choose one) ")
    if user_action.lower() == 'songs':
        print(' ')
        songs(self)
    elif user_action.lower() == 'history':
        print(' ')
        stream_history(self)

def search_data(self):
    pass

def add_data(self):
    new_data = input("Would you like to 'queue' a song, add a 'listener' or"
    + " 'upload' a new song? ")
    if new_data.lower() == 'listener':
        add_listener(self)
    elif new_data.lower() == 'upload':
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
    user_input = input("Enter Your Name: ")
    CLI(user_input)