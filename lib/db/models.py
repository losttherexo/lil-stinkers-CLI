from sqlalchemy import (create_engine, ForeignKey, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()

# artist: name, genre, founded
class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    genre = Column(String(), default = '')
    founded = Column(Integer(), default = '')

    songs = relationship('Song', backref=backref('artist'))

    # def __repr__(self):
    #     return f'Artist {self.id}: {self.name}'
    

# listener: name, age
class Listener(Base):
    __tablename__ = 'listeners'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    

    songs = relationship('Song', backref=backref('listener'))


    def __repr__(self):
        return f'Listener {self.id}: {self.name}, {self.age}'


# song: name, year, stream_count, artist, listener (stretch:link)
class Song(Base):
    __tablename__ = 'songs'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    year = Column(Integer())
    stream_count = Column(Integer(), default = 0)
    artist_id = Column(Integer(), ForeignKey('artists.id'))
    listener_id = Column(Integer(), ForeignKey('listeners.id'))

    # stretch goal below

    # link = Column(String())

    def __repr__(self):
        return f'Song {self.id}: {self.name}'
