#!/usr/bin/python3
"""Script that fetches State object passed as argument from database"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = sys.argv[4]
    st = session.query(State).filter(State.name.like(state)).one()
    if st:
        print(state)
    else:
        print('Not found')
    session.close()
