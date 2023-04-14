#!/usr/bin/python3
"""Script that changes name of State object to database"""

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
    st = session.query(State).filter_by(id=2).first()
    if st:
        st.name = "New Mexico"
    else:
        print('Not found')
    session.commit()
    session.close()
