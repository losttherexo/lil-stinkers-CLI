from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('')
Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    

class Listener(Base):
    __tablename__ = 'listeners'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    name = Column(String)

Base.metadata.create_all(engine)


# artist = Artist(name='Mac Miller')
# session.add(artist)
# session.commit()