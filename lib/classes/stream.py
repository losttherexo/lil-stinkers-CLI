from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Stream

engine = create_engine('sqlite:///db/migrations_test.db')
Session = sessionmaker(bind=engine)
session = Session()

# function that returns most streamed songs?
