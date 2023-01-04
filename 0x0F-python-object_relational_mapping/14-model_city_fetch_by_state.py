#!/usr/bin/python3
"""Retrieve all Cities using ORM"""

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
    for res in session.query(State.name, City.id, City.name).filter(
            City.state_id == State.id).order_by(City.id):
        print('{:s}: ({:d}) {:s}'.format(res[0], res[1], res[2])
