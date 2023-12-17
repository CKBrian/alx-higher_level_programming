#!/usr/bin/python3
"""
Defines a module that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sqlalchemy import create_engine, func

if __name__ == "__main__":
    user, passwd, db, state_name = sys.argv[1:5]
    engn = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db)
    engine = create_engine(engn, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
