#!/usr/bin/python3
"""Retrieve all States using ORM"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]), echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    i = 1
    for state, city in session.query(State.name, City.name).filter(
        City.state_id == State.id):
        print('{}: ({:d}) {}'.format(state, i, city))
        i += 1
