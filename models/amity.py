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
		self.all_rooms = []
		self.living_spaces = []
		self.office_spaces = []
		self.allocated_rooms = []
		self.db_people_list = []
		self.db_room_list = []

	def create_room(self, room):
		'''
		First check that the new room being created does not 
		already exist.
		'''
		for rooms in self.all_rooms:
			if room["room_name"] == rooms.room_name:
				print ("\n"+rooms.room_name.upper()+" already exists. \n")
				return
		if room["room_type"] == "office":
			new_room = OfficeSpace(room["room_name"])
			self.all_rooms.append(new_room)
			self.office_spaces.append(new_room)
			text = ("\n You have added "+new_room.room_name.upper()+" to Office Spaces in Amity \n")
		else:
			new_room = LivingSpace(room["room_name"])
			self.all_rooms.append(new_room)
			self.living_spaces.append(new_room)
			text = ("\n You have added "+new_room.room_name.upper()+" to Living Spaces in Amity \n")
		print (text)

	def create_person(self, person):
		'''
		Once a person is created they are called by the assign person function
		to assign them an office room. 
		If the person is a fellow and wants accomodation, the assign fellow to living space function
		is also called. This is to automate room allocations.
		'''  
		for people in self.all_people:
			if person["person_name"] == people.person:
				print ("\n"+people.person.upper()+" already exists. \n")
				return
		if person["role"] == "staff":
			new_person = Staff(person["person_name"]) 
			self.staff_list.append(new_person)
			print ("\n You have added "+new_person.person.upper()+" as Staff in Amity \n")
		else:
			new_person = Fellow(person["person_name"])
			new_person.accomodation = person["wants_accomodation"]
			self.fellows_list.append(new_person)
			print ("\n You have added "+new_person.person.upper()+" as a Fellow in Amity \n")
			if new_person.accomodation in ["yes", "Y"]:
				self.assign_fellow_to_living_space(new_person)
			else: self.unallocated_people.append(new_person)
		self.all_people.append(new_person)
		self.assign_person_to_office_space(new_person)
		
	def assign_person_to_office_space(self, new_person):
		'''
		This function calls two helper functions in the following way: 
		It first returns a random room then checks if that room's occupancy
		is below the maximum capacity before assigning a person to that random room.
		'''
		if len(self.office_spaces) > 0:
			random_room = self.get_random_room("office")
			if self.is_room_available(random_room) == True:
				if type(new_person) == Staff:
					self.allocated_staff.append(new_person)
				elif type(new_person) == Fellow:
					if new_person not in self.allocated_fellows: self.allocated_fellows.append(new_person)								
				random_room.occupants.append(new_person)
				new_person.assigned_office = random_room.room_name
				self.allocated_people.append(new_person)
				if random_room not in self.allocated_rooms: self.allocated_rooms.append(random_room)
				text = ("\n"+new_person.person.upper()+" has been assigned to "+random_room.room_name.upper()+"\n")
			else:
				text = ("\n"+random_room.room_name.upper()+" is full. "+new_person.person.upper()+" cannot be assigend here. \n")
				if new_person not in self.unallocated_people: self.unallocated_people.append(new_person)
		else:
			text = ("\n There are no offices in Amity. Use the create_room <room_name> function to create one. \n")
			if new_person not in self.unallocated_people: self.unallocated_people.append(new_person)
		print (text)
			
	def assign_fellow_to_living_space(self, new_person):
		if len(self.living_spaces) > 0:
			random_room = self.get_random_room("living")
			if self.is_room_available(random_room) == True:
				random_room.occupants.append(new_person)
				new_person.assigned_living = random_room.room_name
				if new_person not in self.allocated_fellows: self.allocated_fellows.append(new_person)
				if random_room not in self.allocated_rooms: self.allocated_rooms.append(random_room)
				text = ("\n"+new_person.person.upper()+" has been assigned to "+random_room.room_name.upper()+"\n")
			else:
				text = ("\n"+random_room.room_name.upper()+" is full. "+new_person.person.upper()+" cannot be assigend here. \n")
				if new_person not in self.unallocated_people: self.unallocated_people.append(new_person)
		else:
			text = ("\n There are no living rooms in Amity. Use the create_room <room_name> function to create one. \n")
			if new_person not in self.unallocated_people: self.unallocated_people.append(new_person)
		print (text)

	def get_random_room(self, room_type):
		'''
		Randomizes the room selection depending on whether you are searching
		for offices or living spaces respectively. 
		'''
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
			return len(random_room.occupants) < 6
		elif random_room.room_type == "LivingSpace":
			return len(random_room.occupants) < 4

	def reallocate_person(self, person, room_name):
		'''
		First loops through the room objects stored in the all_rooms list and 
		extracts the room names as strings which are then stored in a rooms list
		to allow for comparison.
		'''
		rooms_list = [room.room_name for room in self.all_rooms]
		if room_name not in rooms_list:
			print ("\n"+room_name.upper()+" does not exist. \n")
		elif room_name in [person.assigned_living, person.assigned_office]:
			print ("\n"+person.person.upper()+" is already assigned to "+room_name.upper()+"\n")
		else:
			room = [room for room in self.all_rooms if room.room_name == room_name][0]
			if type(person) == Staff and type(room) == LivingSpace:
				print("\n Staff cannot be assigned to living spaces. \n")
			elif self.is_room_available(room):
				if type(room) == OfficeSpace:
					self.clean_up_office_reallocations(person)
					person.assigned_office = room.room_name
					if person in self.unallocated_people:
					# Check ensures fellows without living spaces are not removed from unallocated
					# people list when reallocated between office spaces. 
						if type(person) == Fellow: pass
						else: self.unallocated_people.remove(person)
				elif type(room) == LivingSpace:
					self.clean_up_living_reallocations(person)
					person.assigned_living = room.room_name
					if person in self.unallocated_people: self.unallocated_people.remove(person)
				room.occupants.append(person)
				if person not in self.allocated_people: self.allocated_people.append(person)
				if room not in self.allocated_rooms: self.allocated_rooms.append(room)
				print ("\n You have reallocated "+person.person.upper()+" to "+room.room_name.upper()+"\n")
			else:
				print ("\n Please try a different room. "+room.room_name+" is full. \n")					
						
	def clean_up_office_reallocations(self, person):
		'''
		This is a helper function that removes people from offices which 
		they have been reallocated away from. 
		'''
		old_office = person.assigned_office
		if old_office == "": pass
		else: 
			room = [room for room in self.all_rooms if room.room_name == old_office][0]
			room.occupants.remove(person)
			return room.occupants

	def clean_up_living_reallocations(self, person):
		'''
		This is a helper function that removes people from living rooms which 
		they have been reallocated away from.
		'''
		old_living = person.assigned_living
		if old_living == "": pass
		else:
			room = [room for room in self.all_rooms if room.room_name == old_living][0]
			room.occupants.remove(person)
			return room.occupants

	def load_people_from_file(self, filename):
			with open("./models/"+filename, mode="r") as text:
				people_list = text.readlines()
				for people in people_list:
					person = people.split()
					person_name = person[0].lower()+" "+person[1].lower()
					role = person[2]
					if role == "STAFF":
						person_dict = {"person_name":person_name, "role":"staff"}
						self.create_person(person_dict)
					if role == "FELLOW":
						accomodation = person[3]
						person_dict = {"person_name":person_name, "role":"fellow", 
						"wants_accomodation":accomodation}
						self.create_person(person_dict)

	def write_allocated_to_terminal(self):
		if len(self.all_rooms) > 0:
			print ("\n Printing allocations to the terminal... \n")
			for room in self.all_rooms:
				text = "\n"+room.room_name.upper()+"\n"
				text = text + ("-"*40 + "\n")			
				if len(room.occupants) > 0:
					text = text + (", ".join([occupant.person.upper() for occupant in room.occupants])+"\n")
				else:
					text = text + ("\n No one has been allocated to this room yet. \n")
				print (text)
		else:
			print ("\n There are currently no allocations. \n")

	def write_allocated_to_file(self, filename):
		print ("\n Printing allocations to txt file: "+filename)
		with open(filename, mode="w", encoding='utf-8') as text:
			for room in self.all_rooms:
				text.write("\n"+room.room_name.upper()+"\n")
				text.write("-"*40 +"\n")			
				if len(room.occupants) > 0:
					text.write(", ".join([occupant.person.upper() for occupant in room.occupants])+"\n")	
				else:
					text.write("No one has been allocated yet. \n")
			
	def write_unallocated_to_terminal(self):
		if len(self.unallocated_people) > 0:
			text = ("\n Printing unallocated people to the terminal... \n")
			text = "\n Unallocated people:"+"\n"
			text = text + ("-"*40 + "\n")
			text = text + (", ".join([person.person.upper() for person in self.unallocated_people])+"\n")
		else: 
			text = ("\n There are currently no unallocated people.\n")
		print (text)
			
	def write_unallocated_to_file(self, filename):
		print ("\n Printing unallocated people to txt file: "+filename)
		with open(filename, mode="w", encoding='utf-8') as text:
			if len(self.unallocated_people) > 0:
				text.write("Unallocated people:"+"\n")
				text.write("-"*40 +"\n")
				text.write(", ".join([person.person.upper() for person in self.unallocated_people]))
			else:
				text.write("There are currently no unallocated people.")

	def print_room(self, room_name):
		if len(self.all_rooms) > 0:
			for room in self.all_rooms:
				if room.room_name == room_name:
					if len(room.occupants) > 0:
						text = ("\n"+room.room_name.upper()+"\n")
						text = text + ("-"*50 +"\n")
						text = text + (", ".join([occupant.person.upper() for occupant in room.occupants])+"\n")
					else:
						text = ("\n This room is empty. \n")
		else:
			text = ("\n There are no rooms yet. \n")	
		print (text)

	def load_rooms_from_db(self, room):
		if room["room_type"] == "OfficeSpace":
			new_room = OfficeSpace(room["room_name"])
			self.office_spaces.append(new_room)
		else:
			new_room = LivingSpace(room["room_name"])
			self.living_spaces.append(new_room)
		self.db_room_list.append(new_room)
		self.all_rooms.append(new_room)

	def load_people_from_db(self, person, assigned_office, assigned_living):
		if person["role"] == "Staff":
			new_person = Staff(person["person_name"])
			new_person.assigned_office = assigned_office
			new_person.assigned_living = assigned_living
			self.staff_list.append(new_person)
			self.allocated_staff.append(new_person)
		else:
			new_person = Fellow(person["person_name"])
			new_person.assigned_office = assigned_office
			new_person.assigned_living = assigned_living
			self.fellows_list.append(new_person)
			self.allocated_fellows.append(new_person)
		self.db_people_list.append(new_person)
		self.all_people.append(new_person)
		self.allocated_people.append(new_person)

	def populate_room_occupants_from_db_load(self):
		'''
		When saving to the database, a room's occupants are stored
		as an integer. When loading the room back to the application, 
		this function repopulates the room's occupant list
		with people names. 
		'''
		for room in self.db_room_list:
			for person in self.db_people_list:
				if person.assigned_office == room.room_name:
					room.occupants.append(person)
				elif person.assigned_living == room.room_name:
					room.occupants.append(person)
				else:
					if "" in [person.assigned_office, person.assigned_living]:
						if person not in self.unallocated_people: self.unallocated_people.append(person)

			
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
	
	def get_list_of_unallocated_people(self):
		return self.unallocated_people
	
	def get_list_of_db_rooms(self):
		return self.db_room_list

	def get_list_of_db_people(self):
		return self.db_people_list
