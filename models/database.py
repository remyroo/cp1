import os
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean


Base = declarative_base()

class Rooms(Base):
	__tablename__ = "rooms"
	id = Column(Integer, primary_key=True, autoincrement=True)
	room_name = Column(String(150), nullable=False, unique=True)
	room_type = Column(String(150), nullable=False)
	room_capacity = Column(Integer, nullable=False)
	room_occupants = Column(Integer, nullable=True)

class People(Base):
	__tablename__ = "people"
	id = Column(Integer, primary_key=True, autoincrement=True)
	person_name = Column(String(150), nullable=False)
	person_role = Column(String(150), nullable=False)
	accomodation = Column(String(100), default=False, nullable = False)
	assigned_office = Column(Integer, nullable=True)
	assigned_living = Column(Integer, nullable=True)
	#rooms = relationship(Rooms)

def create_engine_db(db_name):
    engine = create_engine("sqlite:///models/"+db_name)
    Base.metadata.create_all(engine)






