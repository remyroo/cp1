import os
import unittest
from models.amity import Amity
from models.room import Room
from models.database import *

class RoomTest(unittest.TestCase):

	def setUp(self):
		self.amity = Amity()

	def test_room_creation(self):
		room_list = self.amity.get_list_of_rooms()
		self.assertEqual(len(room_list), 0)
		self.amity.create_room({"room_name":"oculus", "room_type":"office"})
		self.amity.create_room({"room_name":"java", "room_type":"living"})
		self.assertEqual(len(room_list), 2)
	
	def test_office_space_added_to_list_of_offices(self):
	  	room_list = self.amity.get_list_of_office_spaces()
	  	self.assertEqual(len(room_list), 0)
	  	self.amity.create_room({"room_name":"oculus", "room_type":"office"})
	  	self.assertEqual(len(room_list), 1)

	def test_living_space_added_to_list_of_living_spaces(self):
	  	room_list = self.amity.get_list_of_living_spaces()
	  	self.assertEqual(len(room_list), 0)
	  	self.amity.create_room({"room_name":"ruby", "room_type":"living"})
	  	self.assertEqual(len(room_list), 1)

	def test_person_creation(self):
		list_of_people = self.amity.get_list_of_people()
		self.assertEqual(len(list_of_people), 0)
		self.amity.create_person({"person_name":"rehema wachira",
			"role":"fellow",
			"wants_accomodation":"Yes"})
		self.assertEqual(len(list_of_people), 1)

	def test_staff_added_to_staff_list(self):
	  	total_staff_list = self.amity.get_list_of_staff()
	  	self.assertEqual(len(total_staff_list), 0)
	  	self.amity.create_person({"person_name":"anthony nandaa",
			"role":"staff",
			"wants_accomodation":"no"})
	  	self.assertEqual(len(total_staff_list), 1)

	def test_fellow_added_to_fellow_list(self):
	  	total_fellow_list = self.amity.get_list_of_fellows()
	  	self.assertEqual(len(total_fellow_list), 0)
	  	self.amity.create_person({"person_name":"rehema wachira",
			"role":"fellow",
			"wants_accomodation":"no"})
	  	self.assertEqual(len(total_fellow_list), 1)

	def test_people_added_to_allocated_people_list(self):
		self.amity.create_room({"room_name":"oculus", "room_type":"office"})
		self.amity.create_room({"room_name":"java", "room_type":"living"})
		allocation_list = self.amity.get_list_of_allocated_people()
		self.assertEqual(len(allocation_list), 0)
		self.amity.create_person({"person_name":"percila njira",
			"role":"staff",
			"wants_accomodation":"no"})
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.assertEqual(len(allocation_list), 2)

	def test_staff_added_to_allocated_staff_list(self):
		self.amity.create_room({"room_name":"oculus", "room_type":"office"})
		allocated_staff_list = self.amity.get_list_of_allocated_staff()
		self.assertEqual(len(allocated_staff_list), 0)
		self.amity.create_person({"person_name":"percila njira",
			"role":"staff",
			"wants_accomodation":"no"})
		self.assertEqual(len(allocated_staff_list), 1)

	def test_fellow_added_to_allocated_fellow_list(self):
		self.amity.create_room({"room_name":"oculus", "room_type":"office"})
		self.amity.create_room({"room_name":"ruby", "room_type":"living"})
		allocated_fellow_list = self.amity.get_list_of_allocated_fellows()
		self.assertEqual(len(allocated_fellow_list), 0)
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.assertEqual(len(allocated_fellow_list), 1)

	def test_that_staff_assigned_to_office_space_do_not_exceed_six(self):
		self.amity.create_room({"room_name":"oculus", "room_type":"office"})
		oculus = self.amity.get_list_of_rooms()[0]
		self.assertEqual(len(oculus.occupants), 0)
		self.amity.create_person({"person_name":"percila njira",
			"role":"staff",
			"wants_accomodation":"no"})
		self.amity.create_person({"person_name":"jackson saia",
			"role":"staff",
			"wants_accomodation":"no"})
		self.amity.create_person({"person_name":"maureen maina",
			"role":"staff",
			"wants_accomodation":"no"})
		self.amity.create_person({"person_name":"janet njoroge",
			"role":"staff",
			"wants_accomodation":"no"})
		self.amity.create_person({"person_name":"ngibuini mwaura",
			"role":"staff",
			"wants_accomodation":"no"})
		self.amity.create_person({"person_name":"josh mwaura",
			"role":"staff",
			"wants_accomodation":"no"})
		self.amity.create_person({"person_name":"oscar opondo",
			"role":"staff",
			"wants_accomodation":"no"})
		self.assertEqual(len(oculus.occupants), 6)
		
	def test_that_fellows_assigned_to_living_space_do_not_exceed_four(self):
		self.amity.create_room({"room_name": "java", "room_type": "living"})
		java = self.amity.get_list_of_rooms()[0]
		self.assertEqual(len(java.occupants), 0)
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.amity.create_person({"person_name":"japheth obala",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.amity.create_person({"person_name":"rehema wachira",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.amity.create_person({"person_name":"ruth ogendi",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.amity.create_person({"person_name":"elsis sitati",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.assertTrue(len(java.occupants), 4)

	def test_reallocation_of_staff_to_rooms(self):
		self.amity.create_room({"room_name": "oculus", "room_type": "office"})
		self.amity.create_person({"person_name":"percila njira",
			"role":"staff",
			"wants_accomodation":"no"})
		self.amity.create_room({"room_name": "krypton", "room_type": "office"})
		krypton = self.amity.get_list_of_rooms()[1]
		self.assertEqual(len(krypton.occupants), 0)
		self.amity.reallocate_person(self.amity.get_list_of_people()[0], krypton.room_name)
		self.assertEqual(len(krypton.occupants), 1)

	def test_reallocation_of_fellow_to_rooms(self):
		self.amity.create_room({"room_name": "ruby", "room_type": "living"})
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.amity.create_room({"room_name": "java", "room_type": "living"})
		java = self.amity.get_list_of_rooms()[1]
		self.assertEqual(len(java.occupants), 0)
		self.amity.reallocate_person(self.amity.get_list_of_people()[0], java.room_name)
		self.assertEqual(len(java.occupants), 1)

	def test_allocations_are_added_to_allocated_rooms_list(self):
		allocated_list = self.amity.get_list_of_allocated_rooms()
		self.amity.create_room({"room_name":"oculus", "room_type":"office"})
		self.assertEqual(len(allocated_list), 0)
		self.amity.create_person({"person_name":"percila njira",
			"role":"staff",
			"wants_accomodation":"no"})
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"wants_accomodation":"no"})
		self.assertEqual(len(allocated_list), 1)

	def test_allocations_can_be_printed_to_terminal(self):
		self.amity.create_room({"room_name":"oculus", "room_type":"office"})
		self.amity.create_room({"room_name":"ruby", "room_type":"living"})
		self.amity.create_person({"person_name":"percila njira",
			"role":"fellow",
			"wants_accomodation":"no"})
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"wants_accomodation":"no"})
		self.amity.write_allocated_to_terminal()

	def test_allocations_can_be_printed_to_file(self):
		self.amity.create_room({"room_name":"oculus", "room_type":"office"})
		self.amity.create_room({"room_name":"ruby", "room_type":"living"})
		self.amity.create_person({"person_name":"percila njira",
			"role":"fellow",
			"wants_accomodation":"no"})
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"wants_accomodation":"no"})
		self.amity.write_allocated_to_file("allocations.txt")
		
	def test_unallocated_people_are_added_to_unallocated_people_list(self):
		unallocated_list = self.amity.get_list_of_unallocated_people()
		self.assertEqual(len(unallocated_list), 0)
		self.amity.create_person({"person_name":"percila njira",
			"role":"fellow",
			"wants_accomodation":"no"})
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.assertEqual(len(unallocated_list), 2)

	def test_unallocated_people_can_be_printed_to_terminal(self):
		unallocated_list = self.amity.get_list_of_unallocated_people()
		self.amity.create_person({"person_name":"percila njira",
			"role":"fellow",
			"wants_accomodation":"no"})
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.amity.write_unallocated_to_terminal()

	def test_unallocated_people_can_be_printed_to_file(self):
		unallocated_list = self.amity.get_list_of_unallocated_people()
		self.amity.create_person({"person_name":"percila njira",
			"role":"fellow",
			"wants_accomodation":"no"})
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.amity.write_unallocated_to_file("unallocated.txt")

	def test_user_input_room_allocations_can_be_printed_to_terminal(self):
		self.amity.create_room({"room_name":"oculus", "room_type":"office"})
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.amity.create_person({"person_name":"japheth obala",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.amity.create_person({"person_name":"rehema wachira",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.amity.create_person({"person_name":"ruth ogendi",
			"role":"fellow",
			"wants_accomodation":"yes"})
		self.amity.print_room(self.amity.get_list_of_rooms()[0].room_name)

	def test_load_people_from_file(self):
		#Test has new error - can't find load_people.txt file - but functionality works. 
		self.amity.create_room({"room_name":"oculus", "room_type":"office"})
		self.amity.create_room({"room_name": "krypton", "room_type": "office"})
		self.amity.create_room({"room_name":"ruby", "room_type":"living"})
		staff_list = self.amity.get_list_of_allocated_staff()
		fellows_list = self.amity.get_list_of_allocated_fellows()
		self.assertEqual(len(staff_list), 0)
		self.assertEqual(len(fellows_list), 0)
		self.amity.load_people_from_file("load_people.txt")
		self.assertEqual(len(staff_list), 3)
		self.assertEqual(len(fellows_list), 4)

	def test_db_created_when_save_state_called(self):
		# Test has error
		database.create_engine_db("test.db")
		self.assertTrue(os.path.exists("test.db"))
		os.remove("test.db")

	def test_db_rooms_loaded_to_application(self):
		db_room_list = self.amity.get_list_of_db_rooms()
		self.assertEqual(len(db_room_list), 0)
		self.amity.load_rooms_from_db({"room_name":"oculus", "room_type":"office"})
		self.assertEqual(len(db_room_list), 1)		

	def test_db_people_loaded_to_application(self):
		db_people_list = self.amity.get_list_of_db_people()
		self.assertEqual(len(db_people_list), 0)
		self.amity.load_people_from_db({"person_name":"percila njira",
			"role":"fellow",
			"wants_accomodation":"no"}, "oculus", "ruby")
		self.assertEqual(len(db_people_list), 1)



if __name__ == '__main__':
	unittest.main()
	