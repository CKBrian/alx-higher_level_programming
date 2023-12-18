#!/usr/bin/python3
"""
Defines a module that deletes an object
from the database hbtn_0e_6_us
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sqlalchemy import create_engine

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
            session.delete(state)

    session.commit()
    session.close()
