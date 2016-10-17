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
    	room_name = Column(String(150), nullable=False)
    	room_type = Column(String(150), nullable=False)
    	room_capacity = Column(Integer(150), nullable=False)
    	office_occupants = Column(Integer(150), nullable=True)

    class People(Base):
    	__tablename__ = "people"
    	id = Column(Integer, primary_key=True, autoincrement=True)
    	person_name = Column(String(150), nullable=False)
    	person_type = Column(String(150), nullable=False)
    	wants_accomodation = Column(Boolean, nullable = False)
    	assigned_office = Column(Integer(150), ForeignKey("rooms.id"), nullable=True)
    	assigned_living = Column(Integer(150), ForeignKey("rooms.id"), nullable=True)
    	room = relationship(Rooms)

    class Allocations(Base):
    	__tablename__ = "allocations"
    	room = Column(String(150), ForeignKey("rooms.id"))
    	person = Column(String(150), ForeignKey("people.id"))
    	room_allocations = relationship(Rooms)
    	room_occupants = relationship(People)

    




