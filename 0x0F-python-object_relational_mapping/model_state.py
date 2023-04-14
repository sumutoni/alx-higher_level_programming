#!/usr/bin/python3
"""State class that links to states table"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class definition"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=true, nullable=false)
    name = Column(String(128), nullable=false)
