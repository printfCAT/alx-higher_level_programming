#!/usr/bin/python3
""" define a subclass State """


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv


engine = create_engine(f'mysql://{argv[1]}:{argv[2]}@localhost:3306/')
engine.execute(f"CREATE DATABASE IF NOT EXISTS {argv[3]}")
engine = create_engine(f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class State(Base):
    """ subclass State """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
