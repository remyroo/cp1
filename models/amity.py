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
			print ("You have added "+new_room.room_name.upper()+ " to Office Spaces in Amity")
		else:
			new_room = LivingSpace(room["room_name"])
			self.living_spaces.append(new_room)
			print ("You have added "+new_room.room_name.upper()+" to Living Spaces in Amity")
		self.all_rooms.append(new_room)

	def create_person(self, person):
		'''
		Once a person is created they are called by the assign person function
		to assign them an office room. 
		If the person is a fellow and wants accomodation, the assign fellow to living space function
		is also called.
		'''  

		if person["role"] == "staff":
			new_person = Staff(person["person_name"])
			self.staff_list.append(new_person)
			print ("You have added "+new_person.person.upper()+" as Staff in Amity") 
		else:
			new_person = Fellow(person["person_name"])
			new_person.accomodation = person["wants_accomodation"]
			self.fellows_list.append(new_person)
			print ("You have added "+new_person.person.upper()+" as a Fellow in Amity")
			if new_person.accomodation == "yes":
				self.assign_fellow_to_living_space(new_person)
		self.all_people.append(new_person)
		self.assign_person_to_office_space(new_person)
		
	def assign_person_to_office_space(self, new_person):
		'''
		This function calls two helper functions in the following way: 
		It first returns a random room then checks if that room's occupancy
		is below the maximum capacity before assigning a person to that random room.
		'''

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
				self.allocated_rooms.append(random_room)
			print ("You have added "+new_person.person.upper()+" to "+random_room.room_name.upper())
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
			print ("You have added "+new_person.person.upper()+" to "+random_room.room_name.upper())	
			
	def assign_fellow_to_living_space(self, new_person):
		if len(self.living_spaces) > 0:
			random_room = self.get_random_room("living")
			if self.is_room_available(random_room) == True:
				random_room.occupants.append(new_person)
				new_person.assigned_office = random_room.room_name
				self.allocated_fellows.append(new_person)
			else:
				random_room = self.get_random_room("office")
			self.allocated_rooms.append(random_room)
			self.allocated_people.append(new_person)
		print ("You have added "+new_person.person.upper()+" to "+random_room.room_name.upper())

	def get_random_room(self, room_type):
		'''
		Randomizes the room selection depending on whether you are searching
		for offices or living spaces respectively. 
		'''

		random_room = ""
		if room_type == "office":
			random_room = self.office_spaces[random.randint(0, (len(self.office_spaces) -1))]
		else:
			random_room = self.living_spaces[random.randint(0, (len(self.living_spaces) -1))]
		return random_room

	def is_room_available(self, random_room):
		'''
		Checks whether the occupants of a room are less than their respecitve capacities.
		'''

		if random_room.room_type == "OfficeSpace":
			if len(random_room.occupants) < 6:
				return True
			else:
				return False
		elif random_room.room_type == "LivingSpace":
			if len(random_room.occupants) < 4:
				return True
			else:
				return False

	def reallocate_person(self, person, room_name):
		'''
		First loops through the room objects stored in the all_rooms list and 
		extracts the room names as strings which are then stored in a rooms list
		to allow for comparison.
		'''

		rooms = []
		for room in self.all_rooms:
			rooms.append(room.room_name)
		if room_name.strip() not in rooms:
			print ("Room not available")
		elif type(person) == Staff:
			if person.assigned_office == room_name:
				print ("Person is currently assigned to this room")
			else:
				for room in self.all_rooms:
					if room.room_name == room_name and type(room) == OfficeSpace:
						room.occupants.append(person)
						person.assigned_office = room.room_name
						self.allocated_staff.append(person)
						self.allocated_people.append(person)
						print ("You have reallocated "+person.person.upper()+" to "+room.room_name.upper())
					elif room.room_name == room_name and type(room) is not OfficeSpace:
						print("Staff cannot be assigned to living spaces")
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
							print ("You have reallocated "+person.person.upper()+" to "+room.room_name.upper())
						elif type(room) == OfficeSpace:
							person.assigned_office = room.room_name
							print ("You have reallocated "+person.person.upper()+" to "+room.room_name.upper())
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