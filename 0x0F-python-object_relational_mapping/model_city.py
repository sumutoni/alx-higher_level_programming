#!/usr/bin/python3
"""Class Definition of City"""

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """Class definition"""
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __str__(self):
        """Print function"""
        return "{} {} {}".format(self.id, self.state_id, self.name)

    def __repr__(self):
        """object representation"""
        return "City(id={}, state_id={}, name={})".format(
            self.id, self.state_id, self.name)
