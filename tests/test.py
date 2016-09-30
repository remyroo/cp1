import unittest
from app.room import Room
from app.person import Person

class AmityTest(unittest.TestCase):

	def test_room_creation(self):
		room = Room()
		oculus = room.create_room("oculus")
		self.assertTrue(oculus, msg="Room has not been created")

	def test_the_number_of_rooms_created(self):
		room = Room()
		room.create_room("oculus")
		self.assertEqual(room.get_number_of_rooms(), 1)

	def test_assign_room(self):
		room = Room()
		person = Person()
		rehema = person.create_person("rehema")
		oculus = room.create_room("oculus")
		self.assertTrue(room.assign_room(rehema, oculus), msg="Room allocation failed")

	def test_if_room_is_full(self):
		room = Room()
		room_status = room.is_room_full("oculus")
		self.assertTrue(room_status, msg="Room is not full")

	def test_person_creation(self):
		person = Person()
		rehema = person.create_person("rehema")
		self.assertTrue(rehema, msg="Person has not been created")

	# def test_person_role_is_input_correctly(self):
	# 	person = Person()
	# 	rehema = person.create_person("rehema", "fellow")

	def test_the_number_of_people_created(self):
		person = Person()
		person.create_person("rehema")
		self.assertEqual(person.get_number_of_people(), 1)

	def test_person_can_be_reallocated(self):
		person = Person()
		room = Room()
		rehema = person.create_person("rehema")
		oculus = room.create_room("oculus")
		self.assertTrue(person.reallocate_person(rehema, oculus), msg="Person reallocation failed")

	def test_print_names_of_all_people_in_a_specified_room(self):
	# Print the names of all the people in the specified room
		person = Person()
		room = Room()
		oculus = room.create_room("oculus")
		total_occupants_in_room = person.get_list_of_people_in_room("oculus")
		self.assertTrue(total_occupants_in_room, msg="Failed to return list of people in rooms")

	def test_load_people_and_assign_them_rooms(self):
	# Adds people to rooms from a text file
		person = Person()
		self.assertTrue(person.load_people("file_a.txt"), msg="File did not load")

	def test_print_list_of_room_allocations(self):
	# Prints a list of allocations
		person = Person()
		self.assertTrue(person.print_room_allocations("file_a.txt"), msg="Room allocation list did not load")

	def test_print_list_of_unallocated_people(self):
		person = Person()
		self.assertTrue(person.print_unallocated_people("file_a.txt"), msg="List of unallocated people did not load")

	

if __name__ == '__main__':
	unittest.main()