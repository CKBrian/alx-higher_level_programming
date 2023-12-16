#!/usr/bin/python3
"""
Defines a module which contains the class definition of a
State and an instance Base = declarative_base()
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys


user = sys.argv[1]
passwd = sys.argv[2]
db = sys.argv[3]

# Create an engine to connect to database
engn = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db)
engine = create_engine(engn, pool_pre_ping=True)

Base = declarative_base()


class State(Base):
    """ Defines the structure of the states table in hbtn_0e_6_usa """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)  # Create table

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()
