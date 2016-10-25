from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.database import *
from models.amity import Amity

amity = Amity()

class Database(object):

	def save_state(self, db_name):
		engine = create_engine_db(db_name)
		Base.metadata.bind = engine
		DBSession = sessionmaker(bind=engine)
		session = DBSession()

		db_rooms_table = session.query(Rooms).all()
		db_rooms = [db_room.room_name for db_room in db_rooms_table]	
		if len(amity.all_rooms) > 0:
			for room in amity.all_rooms:
				if room.room_name in db_rooms:
					session.query(Rooms).filter_by(room_name=room.room_name).update({Rooms.room_occupants: len(room.occupants)})
					session.commit()
				else:
					new_room = Rooms()
					new_room.room_name = room.room_name
					new_room.room_type = room.room_type
					new_room.room_capacity = room.capacity
					new_room.room_occupants = len(room.occupants)
					session.add(new_room)
					session.commit()
		else:
			print ("\n There are currently no rooms to save \n")

		db_people_table = session.query(People).all()
		db_people = [db_person.person_name for db_person in db_people_table]
		if len(amity.all_people) > 0:
			for person in amity.all_people:
				if person.person in db_people: 
					session.query(People).filter_by(person_name=person.person).update({People.assigned_office: person.assigned_office})
					session.query(People).filter_by(person_name=person.person).update({People.assigned_living: person.assigned_living})
					session.commit()
				else:
					new_person = People()
					new_person.person_name = person.person
					new_person.person_role = person.role
					new_person.accomodation = person.accomodation
					new_person.assigned_office = person.assigned_office
					new_person.assigned_living = person.assigned_living
					session.add(new_person)
					session.commit()
		else:
			print ("\n There are currently no people to save \n")

	def load_state(self, db_name):
		self.engine = create_engine_db(db_name)
		engine = create_engine("sqlite:///"+db_name)
		Base.metadata.bind = engine
		DBSession = sessionmaker(bind=engine)
		session = DBSession()

		db_rooms_table = session.query(Rooms).all()
		for db_room in db_rooms_table:
			amity.load_rooms_from_db({"room_name":db_room.room_name, 
				"room_type":db_room.room_type})

		db_people_table = session.query(People).all()
		for db_person in db_people_table:
			amity.load_people_from_db({"person_name":db_person.person_name,
				"role":db_person.person_role,
				"wants_accomodation":db_person.accomodation}, 
				db_person.assigned_office, db_person.assigned_living)

		amity.populate_room_occupants_from_db_load()

