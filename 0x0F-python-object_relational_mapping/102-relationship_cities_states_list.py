#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}\
        '.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    tmp = session.query(City, State)
    tmp1 = tmp.filter(City.state_id == State.id).order_by(City.id)
    for city, state in tmp1:
        print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()
