#!/usr/bin/python3
"""
Defines a module that  lists all City objects, and
corresponding State in the database hbtn_0e_100_usa
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

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
