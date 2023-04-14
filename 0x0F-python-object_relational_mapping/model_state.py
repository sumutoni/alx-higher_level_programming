#!/usr/bin/python3
"""State class that links to states table"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class definition"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __str__(self):
        """Method to print object"""
        return "{}: {}".format(self.id, self.name)
