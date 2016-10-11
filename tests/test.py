import unittest
from models.amity import Amity
from models.room import Room

class RoomTest(unittest.TestCase):

	def setUp(self):
		self.amity = Amity()

	def test_room_creation(self):
		room_list = self.amity.get_list_of_rooms()
		self.assertEqual(len(room_list), 0)
		self.amity.create_room({"room_name": "oculus", "room_type": "office"})
		self.amity.create_room({"room_name": "java", "room_type": "living"})
		self.assertEqual(len(room_list), 2)
	
	def test_office_space_added_to_list_of_offices(self):
	  	room_list = self.amity.get_list_of_office_spaces()
	  	self.assertEqual(len(room_list), 0)
	  	self.amity.create_room({"room_name": "oculus", "room_type": "office"})
	  	self.assertEqual(len(room_list), 1)

	def test_living_space_added_to_list_of_living_spaces(self):
	  	room_list = self.amity.get_list_of_living_spaces()
	  	self.assertEqual(len(room_list), 0)
	  	self.amity.create_room({"room_name": "ruby", "room_type": "living"})
	  	self.assertEqual(len(room_list), 1)

	def test_person_creation(self):
		list_of_people = self.amity.get_list_of_people()
		self.assertEqual(len(list_of_people), 0)
		self.amity.create_person({"person_name":"rehema wachira",
			"role":"fellow",
			"accomodation":"Yes"})
		self.assertEqual(len(list_of_people), 1)

	def test_staff_added_to_staff_list(self):
	  	total_staff_list = self.amity.get_list_of_staff()
	  	self.assertEqual(len(total_staff_list), 0)
	  	self.amity.create_person({"person_name":"anthony nandaa",
			"role":"staff",
			"accomodation":"No"})
	  	self.assertEqual(len(total_staff_list), 1)

	def test_fellow_added_to_fellow_list(self):
	  	total_fellow_list = self.amity.get_list_of_fellows()
	  	self.assertEqual(len(total_fellow_list), 0)
	  	self.amity.create_person({"person_name":"rehema wachira",
			"role":"fellow",
			"accomodation":"No"})
	  	self.assertEqual(len(total_fellow_list), 1)

	def test_people_added_to_allocated_people_list(self):
		self.amity.create_room({"room_name": "oculus", "room_type": "office"})
		self.amity.create_room({"room_name": "java", "room_type": "living"})
		allocation_list = self.amity.get_list_of_allocated_people()
		self.assertEqual(len(allocation_list), 0)
		self.amity.create_person({"person_name":"percila njira",
			"role":"staff",
			"accomodation":"No"})
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"accomodation":"No"})
		self.assertEqual(len(allocation_list), 2)

	def test_staff_added_to_allocated_staff_list(self):
		self.amity.create_room({"room_name": "oculus", "room_type": "office"})
		self.amity.create_room({"room_name": "valhalla", "room_type": "office"})
		self.amity.create_room({"room_name": "krypton", "room_type": "office"})
		allocation_list = self.amity.get_list_of_allocated_staff()
		self.assertEqual(len(allocation_list), 0)
		self.amity.create_person({"person_name":"percila njira",
			"role":"staff",
			"accomodation":"No"})
		self.assertEqual(len(self.amity.allocated_staff), 1)

	def test_fellow_added_to_allocated_fellow_list(self):
		self.amity.create_room({"room_name": "ruby", "room_type": "living"})
		allocation_list = self.amity.get_list_of_allocated_fellows()
		self.assertEqual(len(allocation_list), 0)
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"accomodation":"No"})
		self.assertEqual(len(self.amity.allocated_fellows), 1)

	## THIS TEST DOESNT WORK
	def test_that_staff_are_assigned_to_office_spaces(self):
		self.amity.create_room({"room_name": "oculus", "room_type": "office"})
		self.amity.create_room({"room_name": "krypton", "room_type": "office"})
		self.assertEqual(len(allocated_room_list), 0)
		self.amity.create_person({"person_name":"percila njira",
			"role":"staff",
			"accomodation":"No"})
		self.amity.create_person({"person_name":"jackson saia",
			"role":"staff",
			"accomodation":"No"})
		self.amity.create_person({"person_name":"maureen maina",
			"role":"staff",
			"accomodation":"No"})
		self.amity.create_person({"person_name": "janet njoroge",
			"role":"staff",
			"accomodation":"No"})
		self.amity.create_person({"person_name": "ngibuini mwaura",
			"role":"staff",
			"accomodation":"No"})
		self.amity.create_person({"person_name": "josh mwaura",
			"role":"staff",
			"accomodation":"No"})
		self.amity.create_person({"person_name": "oscar opondo",
			"role":"staff",
			"accomodation":"No"})
		self.assertEqual(len(allocated_room_list), 2)


	## THIS TEST DOESNT WORK
	def test_that_living_allocation_is_randomized(self):
		self.amity.create_room({"room_name": "java", "room_type": "living"})
		self.amity.create_room({"room_name": "ruby", "room_type": "living"})
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"accomodation":"No"})
		self.amity.create_person({"person_name":"japheth obala",
			"role":"fellow",
			"accomodation":"No"})
		self.amity.create_person({"person_name":"rehema wachira",
			"role":"fellow",
			"accomodation":"No"})
		self.amity.create_person({"person_name": "ruth ogendi",
			"role":"fellow",
			"accomodation":"No"})
		self.amity.create_person({"person_name": "elsis sitati",
			"role":"fellow",
			"accomodation":"No"})
		self.amity.create_person({"person_name": "arnold okoth",
			"role":"fellow",
			"accomodation":"No"})
		self.assertTrue(len(self.amity.allocated_rooms), 2)

	def test_unallocated_person_list_increases_when_room_is_full(self):
		pass

	def test_reallocation_of_staff_to_rooms(self):
		self.amity.create_room({"room_name": "oculus", "room_type": "office"})
		self.amity.create_person({"person_name":"percila njira",
			"role":"staff",
			"accomodation":"No"})
		self.amity.create_room({"room_name": "krypton", "room_type": "office"})
		self.amity.reallocate_person(self.amity.get_list_of_people()[0], "krypton")

	def test_reallocation_of_fellow_to_rooms(self):
		self.amity.create_room({"room_name": "oculus", "room_type": "office"})
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"accomodation":"No"})
		self.amity.create_room({"room_name": "krypton", "room_type": "office"})
		self.amity.reallocate_person(self.amity.get_list_of_people()[0], "krypton")
		
	




if __name__ == '__main__':
	unittest.main()