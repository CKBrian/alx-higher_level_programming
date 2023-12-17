#!/usr/bin/python3
"""
Defines a module which contains class defination of a City
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class City(Base):
	""" defines a City class that inherits from Base class"""
	__tablename__ = "cities"

	id = Column(Integer, autoincrement=True, nullable=False, Primary_Key=True, unique=True)
	name = Column(String(128), nullable=False)
	state_id = Column(Integer, nullable=False, ForeignKey=("states.id"))
