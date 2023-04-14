#!/usr/bin/python3
"""Script that list all cities objects from database"""

from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id):
        print(state.name + ": " + city)
    session.close()
