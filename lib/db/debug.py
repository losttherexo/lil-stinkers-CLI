#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Artist, Listener, Song
import ipdb



if __name__ == '__main__':
    
    engine = create_engine('sqlite:///migrations_test.db')
    Session = sessionmaker(bind=engine)
    session = Session()

ipdb.set_trace()