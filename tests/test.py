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
		allocation_list = self.amity.get_list_of_allocated_staff()
		self.assertEqual(len(allocation_list), 0)
		self.amity.create_person({"person_name":"percila njira",
			"role":"staff",
			"accomodation":"No"})
		self.assertEqual(len(self.amity.allocated_staff), 1)

	def test_fellow_added_to_allocated_fellow_list(self):
		self.amity.create_room({"room_name": "oculus", "room_type": "office"})
		allocation_list = self.amity.get_list_of_allocated_fellows()
		self.assertEqual(len(allocation_list), 0)
		self.amity.create_person({"person_name":"samuel gaamuwa",
			"role":"fellow",
			"accomodation":"No"})
		self.assertEqual(len(self.amity.allocated_fellows), 1)

	def test_if_room_is_full(self):
		self.amity.create_room({"room_name": "java", "room_type": "living"})
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
		self.assertRaises("Too many people", self.amity.room_empty(new_room))


	def test_reallocation_of_people_to_rooms(self):
		pass
	




if __name__ == '__main__':
	unittest.main()