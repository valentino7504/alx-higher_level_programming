#!/usr/bin/python3
'''

SQL Alchemy ORM method to fetch first state from the database

'''
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


if __name__ == "__main__":
    argv = sys.argv
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}" +
                           f"@localhost:3306/{argv[3]}", pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()
    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")
