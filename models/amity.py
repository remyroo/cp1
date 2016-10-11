import random
from models.room import OfficeSpace
from models.room import LivingSpace
from models.person import Staff
from models.person import Fellow

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
		self.allocated_rooms = []
		self.unallocated_living = []
		self.unallocated_office = []

	def create_room(self, room):
		if room["room_type"] == "office":
			new_room = OfficeSpace(room["room_name"])
			self.office_spaces.append(new_room)
			#print (("You have added %s to office spaces in amity") % new_room)
		else:
			new_room = LivingSpace(room["room_name"])
			self.living_spaces.append(new_room)
			#print (("You have added %s to living spaces in amity") % new_room)
		self.all_rooms.append(new_room)

	def create_person(self, person):
		if person["role"] == "staff":
			new_person = Staff(person["person_name"])
			self.staff_list.append(new_person)
			#print (("You have added %s to staff in amity") % new_person)
		else:
			new_person = Fellow(person["person_name"])
			self.fellows_list.append(new_person)
			#print (("You have added %s to fellows in amity") % new_person)
			if new_person.accomodation == "yes":
				self.assign_fellow_to_living_space(new_person)
		self.all_people.append(new_person)
		self.assign_person_to_office_space(new_person)
		
	def assign_person_to_office_space(self, new_person):
		if type(new_person) == Staff:
			if len(self.office_spaces) > 0:
				random_room = self.get_random_room("office")
				if self.is_room_available(random_room) == True:
					random_room.occupants.append(new_person)
					new_person.assigned_office = random_room.room_name
					self.allocated_staff.append(new_person)
					self.allocated_people.append(new_person)
				else:
					random_room = self.get_random_room("office")
		elif type(new_person) == Fellow:
			if len(self.office_spaces) > 0:
				random_room = self.get_random_room("office")
				if self.is_room_available(random_room) == True:
					random_room.occupants.append(new_person)
					new_person.assigned_office = random_room.room_name
					self.allocated_fellows.append(new_person)
					self.allocated_people.append(new_person)
				else:
					random_room = self.get_random_room("office")
		self.allocated_rooms.append(random_room)	
			
	def assign_fellow_to_living_space(self, new_person):
		if len(self.living_spaces) > 0:
			random_room = self.get_random_room("living")
			if self.is_room_available(random_room) == True:
					random_room.occupants.append(new_person)
					new_person.assigned_office = random_room.room_name
					self.allocated_fellows.append(new_person)
					self.allocated_people.append(new_person)
			else:
				random_room = self.get_random_room("office")

	def get_random_room(self, room_type):
		random_room = ""
		if room_type == "office":
			random_room = self.office_spaces[random.randint(0, (len(self.office_spaces) -1))]
		else:
			random_room = self.living_spaces[random.randint(0, (len(self.living_spaces) -1))]
		return random_room

	def is_room_available(self, random_room):
		if random_room.room_type == "OfficeSpace":
			if len(random_room.occupants) < 3:
				return True
			else:
				return False
		elif random_room.room_type == "LivingSpace":
			if len(random_room.occupants) < 4:
				return True
			else:
				return False

	def reallocate_person(self, person, room_name):
		rooms = []
		for room in self.all_rooms:
			if room.room_name == room_name:
				rooms.append(room.room_name)
		if room_name not in rooms:
			print ("Room not available")
		elif type(person) == Staff:
			if person.assigned_office == room_name:
				print ("Person is currently assigned to this room")
			else:
				for room in self.all_rooms:
					if room.room_name == room_name:
						room.occupants.append(person)
						person.assigned_office = room.room_name
						self.allocated_staff.append(person)
						self.allocated_people.append(person)
		elif type(person) == Fellow:
			if person.assigned_office == room_name:
				print ("Person is currently assigned to this office")
			elif person.assigned_living == room_name:
				print ("Person is currently assigned to this living space")
			else:
				for room in self.all_rooms:
					if room.room_name == room_name:
						if type(room) == LivingSpace:
							person.assigned_living = room.room_name
						elif type(room) == OfficeSpace:
							person.assigned_office = room.room_name
					room.occupants.append(person)
					self.allocated_fellows.append(person)
					self.allocated_people.append(person)
			print (room.occupants)
		
	def load_people(self, filname):
			pass

	def get_list_of_rooms(self):
		return self.all_rooms	

	def get_list_of_living_spaces(self):
		return self.living_spaces

	def get_list_of_office_spaces(self):
		return self.office_spaces

	def get_list_of_allocated_rooms(self):
		return self.allocated_rooms

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