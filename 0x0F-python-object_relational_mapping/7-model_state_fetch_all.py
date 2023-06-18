#!/usr/bin/python3
""" define subclass State """


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

engine = create_engine(f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
Session = sessionmaker(bind=engine)
session = Session()
states = session.query(State).all()
for state in states:
    print("{}: {}".format(state.id, state.name))
session.close()
