from sqlalchemy import (create_engine, ForeignKey, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

engine = create_engine('sqlite:///playlist.db')

Base = declarative_base()

# song: name, artist, released
class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    artist = Column(String())
    year = Column(Integer(), default = '')

    streams = relationship('Stream', backref=backref('song'))

    def __repr__(self):
        return f'{self.name} by {self.artist}'
    

# listener: name, age
class Listener(Base):
    __tablename__ = 'listeners'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    

    streams = relationship('Stream', backref=backref('listener'))


    def __repr__(self):
        return f'Listener {self.id}: {self.name}, {self.age}'


# Stream: song, listener (stretch:link)
class Stream(Base):
    __tablename__ = 'streams'
    
    id = Column(Integer(), primary_key=True)
    song_name =Column(String())
    song_id = Column(Integer(), ForeignKey('songs.id'))
    listener_id = Column(Integer(), ForeignKey('listeners.id'))

    # stretch goal below

    # link = Column(String())

    def __repr__(self):
        return f'Stream {self.id}: {self.song_id.name} streamed by {self.listener_id.name}'
