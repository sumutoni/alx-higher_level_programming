#!/usr/bin/python3
"""Retrieve all States using ORM"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]), echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State.id).filter(
        State.name == sys.argv[4]).order_by(State.id).all()
    if states:
        for state in states:
            print(state[0])
    else:
        print('Not found')
