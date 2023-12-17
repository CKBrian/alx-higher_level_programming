#!/usr/bin/python3
"""
Defines a module that lists all State objects that contain the letter
a from the database hbtn_0e_6_us
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

    state1 = State(name="Louisiana")
    session.add(state1)
    session.commit()

    state = session.query(State).filter(State.name == "Louisiana").first()
    if state:
        print("{}".format(state.id))

    session.close()
