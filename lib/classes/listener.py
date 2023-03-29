from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Listener

engine = create_engine('sqlite:///db/migrations_test.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_listener(self):
    print(' ')
    name = input('Name: ')
    age = input('Age: ')
    new_listener = Listener(name = name, age = age)

    session.add(new_listener)
    session.commit()

    self.listeners.append(new_listener)