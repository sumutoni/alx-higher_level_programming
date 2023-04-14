#!/usr/bin/python3
"""Script that adds 'Louisiana' State object to database"""

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
    state = State(name="Louisiana")
    session.add(state)
    st = session.query(State).filter(State.name.like(state.name))
    if st:
        print(st.id)
    else:
        print('Not found')
    session.commit()
    session.close()
