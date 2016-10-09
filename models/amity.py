import random
from room import OfficeSpace
from room import LivingSpace
from person import Staff
from person import Fellow

class Amity(object):

	def __init__(self):
		self.all_people = []
		self.staff_list = []
		self.fellows_list = []
		self.allocated_people = []
		self.allocated_staff = []
		self.allocated_fellows = []
		self.unallocated_people = []
		self.unallocated_staff = []
		self.unallocated_fellows = []
		self.all_rooms = []
		self.living_spaces = []
		self.office_spaces = []
		self.unallocated_living = []
		self.unallocated_office = []

	def create_room(self, room):
		if room["room_type"] == "office":
			new_room = OfficeSpace(room["room_name"])
			self.office_spaces.append(new_room)
			print ("You have added %s to office spaces in amity") % new_room
		else:
			new_room = LivingSpace(room["room_name"])
			self.living_spaces.append(new_room)
			print ("You have added %s to living spaces in amity") % new_room
		self.all_rooms.append(new_room)

	def create_person(self, person):
		if person["role"] == "fellow":
			new_person = Fellow(person["person_name"])
			self.fellows_list.append(new_person)
			print ("You have added %s to fellows in amity") % new_person
		else:
			new_person = Staff(person["person_name"])
			self.staff_list.append(new_person)
			print ("You have added %s to staff in amity") % new_person
		self.all_people.append(new_person)
		self.assign_person(new_person)

	def assign_person(self, new_person):
		for room in self.all_rooms:
			#RANDOMIZE THE ROOM HERE!!!!
			if self.room_empty(room):
				if type(new_person) == Staff and type(room) == OfficeSpace:
					self.allocated_staff.append(new_person)
					room.occupants.append(new_person)
					self.allocated_people.append(new_person)
				elif type(new_person) == Fellow and type(room) == LivingSpace:
					self.allocated_fellows.append(new_person)
					room.occupants.append(new_person)
					self.allocated_people.append(new_person)
			else:
				print ("All rooms are full")

	def randomize_room_selection(self, all_rooms):
		random_room = all_rooms[random.randint(0, (len(self.all_rooms) -1))]
		return random_room

	def room_empty(self, room):
		if room.room_type == "OfficeSpace":
			return len(room.occupants) < 6
		elif room.room_type == "LivingSpace":
			return len(room.occupants) < 4

	def get_list_of_rooms(self):
		return self.all_rooms	

	def get_list_of_living_spaces(self):
		return self.living_spaces

	def get_list_of_office_spaces(self):
		return self.office_spaces

	def get_list_of_people(self):
		return self.all_people

	def get_list_of_staff(self):
		return self.staff_list

	def get_list_of_fellows(self):
		return self.fellows_list

	def get_list_of_allocated_people(self):
		return self.allocated_people

	def get_list_of_allocated_staff(self):
		return self.allocated_staff

	def get_list_of_allocated_fellows(self):
		return self.allocated_fellows

	def reallocate_person(self, name, room_name):
		pass

	def load_people(self, filname):
		pass

	# def all_rooms(self):
	# 	# write a function that adds office space and living space 
	# 	# to return a full list. 
	# 	all_rooms = (len(self.living_spaces) + len(self.office_spaces))
	# 	return all_rooms