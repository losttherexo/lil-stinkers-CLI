from sqlalchemy import (create_engine, ForeignKey, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer(), primary_key=True)
    name = Column(String())

    songs = relationship('Song', backref=backref('artist'))

    def __repr__(self):
        return f'Artist {self.id}: {self.name}'
    

class Listener(Base):
    __tablename__ = 'listeners'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    songs = relationship('Song', backref=backref('listener'))


    def __repr__(self):
        return f'Listener {self.id}: {self.name}'


class Song(Base):
    __tablename__ = 'songs'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    artist_id = Column(Integer(), ForeignKey('artists.id'))
    listener_id = Column(Integer(), ForeignKey('listeners.id'))

    def __repr__(self):
        return f'Song {self.id}: {self.name}'
