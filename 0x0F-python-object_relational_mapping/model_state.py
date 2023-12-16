#!/usr/bin/python3
"""
Defines a module which contains the class definition of a
State and an instance Base of declarative_base
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys


Base = declarative_base()


class State(Base):
    """ Defines the structure of the states table in hbtn_0e_6_usa """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
