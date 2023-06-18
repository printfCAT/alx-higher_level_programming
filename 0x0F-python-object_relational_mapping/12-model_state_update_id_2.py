#!/usr/bin/python3
""" define subclass State """


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(f'mysql://{argv[1]}:{argv[2]}\
                            @localhost:3306/{argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State)
    for state in results:
        if state.id == 2:
            state.name = 'New Mexico'
    session.commit()
