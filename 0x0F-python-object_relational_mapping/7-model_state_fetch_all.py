#!/usr/bin/python3
"""Retrieve all States using ORM"""

from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_al(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for id, name in session.query(State.id, State.name).order_by(State.id):
        print("{}: {}".format(id, name))
