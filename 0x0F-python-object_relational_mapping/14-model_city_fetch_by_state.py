#!/usr/bin/python3
'''

Updates the state whose id is 2

'''
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


if __name__ == "__main__":
    argv = sys.argv
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}" +
                           f"@localhost:3306/{argv[3]}", pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State.name, City.id,
                            City.name).join(State).order_by(City.id)
    for row in results:
        print(f"{row[0]}: ({row[1]}) {row[2]}")
