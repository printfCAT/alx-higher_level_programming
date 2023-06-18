#!/usr/bin/python3
""" define a subclass City """


from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class City(Base):
    """ subclass City """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=True)
    state = relationship("State")
