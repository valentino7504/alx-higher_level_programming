#!/usr/bin/python3
'''

Inserts the state "Louisiana" into the states table

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
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    states = session.query(State)
    print(states.count())
