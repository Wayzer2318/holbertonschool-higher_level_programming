#!/usr/bin/python3
'''
Script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
'''
from re import search
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    search = argv[4]

    Session = sessionmaker(bind=engine)
    session = Session()

    if session.query(State).filter(
            State.name == search).order_by(State.id).count() > 0:
        for result in session.query(State).filter(
                State.name == search).order_by(State.id):
            print(result.id)
    else:
        print('Not found')
    session.close()
