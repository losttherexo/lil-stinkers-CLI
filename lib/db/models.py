from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///migrations_test.db')
Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'Artist {self.id}: {self.name}'
    

class Listener(Base):
    __tablename__ = 'listeners'
    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'Listener {self.id}: {self.name}'


class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'Song {self.id}: {self.name}'


Base.metadata.create_all(engine)
