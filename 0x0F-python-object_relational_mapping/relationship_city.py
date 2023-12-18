#!/usr/bin/python3
"""
Defines a module which contains class defination of a City
"""
from relationship_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """ defines a City class that inherits from Base class"""
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, nullable=False,
                primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State")
