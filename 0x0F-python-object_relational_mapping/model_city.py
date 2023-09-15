#!/usr/bin/python3
'''

Creates a City class model for the db

'''


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    '''
    A city class for the ORM project
    '''
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
