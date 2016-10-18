from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.database import *
from models.amity import Amity

amity = Amity()

class Database(object):

	def save_state(self, db_name):
		self.engine = create_engine_db(db_name)
		engine = create_engine("sqlite:///models/"+db_name)
		Base.metadata.bind = engine
		DBSession = sessionmaker(bind=engine)
		session = DBSession()
		
		if len(amity.all_rooms) > 0:
			for room in amity.all_rooms:
				new_room = Rooms()
				new_room.room_name = room.room_name
				new_room.room_type = room.room_type
				new_room.room_capacity = room.capacity
				new_room.room_occupants = len(room.occupants)
				session.add(new_room)
				session.commit()
		else:
			print ("There are currently no rooms to save")

		if len(amity.all_people) > 0:
			for person in amity.all_people:
				new_person = People()
				new_person.person_name = person.person
				new_person.person_role = person.role
				new_person.accomodation = person.accomodation
				new_person.assigned_office = person.assigned_office
				new_person.assigned_living = person.assigned_living
				session.add(new_person)
				session.commit()
		else:
			print ("There are currently no people to save")

	def load_state(self, db_name):
		self.engine = create_engine_db(db_name)
		engine = create_engine("sqlite:///models/"+db_name)
		Base.metadata.bind = engine
		DBSession = sessionmaker(bind=engine)
		session = DBSession()		

		
