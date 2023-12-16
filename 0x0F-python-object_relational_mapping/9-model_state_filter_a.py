#!/usr/bin/python3
"""
Defines a module that lists all State objects that contain the letter
a from the database hbtn_0e_6_us
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sqlalchemy import create_engine, func

if __name__ == "__main__":
    user, passwd, db = sys.argv[1:4]
    engn = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db)
    engine = create_engine(engn, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()
    for state in states:
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))

    session.close()
