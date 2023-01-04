#!/usr/bin/python3
"""Class Definition of State"""

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class definition"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    def __str__(self):
        """Print function"""
        return "{}: {}".format(self.id, self.name)

    def __repr__(self):
        """object representation"""
        return "State(id={}, name={})".format(self.id, self.name)
