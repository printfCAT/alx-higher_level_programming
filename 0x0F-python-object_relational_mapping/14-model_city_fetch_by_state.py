#!/usr/bin/python3
""" define subclass State """


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine(f'mysql://{argv[1]}:{argv[2]}\
                            @localhost:3306/{argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).join(City).order_by(City.id.asc()).all()
    for state in results:
        for city in state.cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
