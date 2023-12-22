#!/usr/bin/python3
"""
Defines a module that  creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy import create_engine

if __name__ == "__main__":
    user, passwd, db = sys.argv[1:4]
    engn = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db)
    engine = create_engine(engn, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state1 = State(name="California")
    city1 = City(name="San Francisco")
    state1.cities.append(city1)
    session.add(state1)
    session.commit()

    session.close()
