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
    states = session.query(State)
    match_found = False
    for state in states:
        if state.name == argv[4]:
            print(state.id)
            Match_found = True
            break
    if match_found is False:
        print("Not found")
