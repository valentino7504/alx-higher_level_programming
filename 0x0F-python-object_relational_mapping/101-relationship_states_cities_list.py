#!/usr/bin/python3
'''

Adds a new city

'''
from relationship_city import City
from relationship_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


if __name__ == "__main__":
    argv = sys.argv
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}" +
                           f"@localhost:3306/{argv[3]}", pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print(f"{state.id}: {state.name}")
        cities = session.query(City).filter(City.state_id
                                            == state.id).order_by(City.id)
        for city in cities:
            print(f"\t{city.id}: {city.name}")
    session.close()
