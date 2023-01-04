#!/usr/bin/python3
"""Class Definition of City"""

import sys
from model_state import Base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey



class City(Base):
    """Class definition"""
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))

    def __str__(self):
        """Print function"""
        return "{} {} {}".format(self.id, self.state_id, self.name)

    def __repr__(self):
        """object representation"""
        return "City(id={}, state_id={}, name={})".format(self.id, self.state_id, self.name)
