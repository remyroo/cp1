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

	def create_room(self, room):
		if room["room_type"] == "office":
			new_room = OfficeSpace(room["room_name"])
			self.office_spaces.append(new_room)
			text = ("\n You have added "+new_room.room_name.upper()+" to Office Spaces in Amity \n")
		else:
			new_room = LivingSpace(room["room_name"])
			self.living_spaces.append(new_room)
			text = ("\n You have added "+new_room.room_name.upper()+" to Living Spaces in Amity \n")
		print (text)
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
			print ("\n You have added "+new_person.person.upper()+" as Staff in Amity") 
		else:
			new_person = Fellow(person["person_name"])
			new_person.accomodation = person["wants_accomodation"]
			self.fellows_list.append(new_person)
			print ("\n You have added "+new_person.person.upper()+" as a Fellow in Amity")
			if new_person.accomodation == "yes" or new_person.accomodation == "Y":
				self.assign_fellow_to_living_space(new_person)
			else:
				self.unallocated_people.append(new_person)
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
					if random_room not in self.allocated_rooms: self.allocated_rooms.append(random_room)
					text = (new_person.person.upper()+" has been assigned to "+random_room.room_name.upper()+"\n")
				else:
					text = ("\n"+random_room.room_name.upper()+" is full. "+new_person.person.upper()+" cannot be assigend here. \n")
					if new_person not in self.unallocated_people: self.unallocated_people.append(new_person)
					# random_room = self.get_random_room("office")
					# self.assign_person_to_office_space(new_person) --> this creates a stack overflow error 
				    # ie RecursionError: maximum recursion depth exceeded while calling a Python object	
				print (text)
			else:
				print ("There are no offices in Amity. Use the create_room <room_name> function to create one.")
				if new_person not in self.unallocated_people: self.unallocated_people.append(new_person)
		elif type(new_person) == Fellow:
			if len(self.office_spaces) > 0:
				random_room = self.get_random_room("office")
				if self.is_room_available(random_room) == True:
					random_room.occupants.append(new_person)
					new_person.assigned_office = random_room.room_name
					if new_person not in self.allocated_fellows: self.allocated_fellows.append(new_person)
					self.allocated_people.append(new_person)
					if random_room not in self.allocated_rooms: self.allocated_rooms.append(random_room)
					text = (new_person.person.upper()+" has been assigned to "+random_room.room_name.upper()+"\n")
				else:
					text = ("\n"+random_room.room_name.upper()+" is full. "+new_person.person.upper()+" cannot be assigend here. \n")
					if new_person not in self.unallocated_people: self.unallocated_people.append(new_person)
					# random_room = self.get_random_room("office")
					# self.assign_person_to_office_space(new_person)
				print (text)
			else:
				print ("There are no offices in Amity. Use the create_room <room_name> function to create one.")
				if new_person not in self.unallocated_people: self.unallocated_people.append(new_person)
			
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
				# random_room = self.get_random_room("living")
				# self.assign_fellow_to_living_space(new_person)
			print (text)
		else:
			print ("There are no living rooms in Amity. Use the create_room <room_name> function to create one.")
			if new_person not in self.unallocated_people: self.unallocated_people.append(new_person)

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
		if room_name not in rooms:
			print ("\n"+room_name.upper()+" is not available. \n")
		elif type(person) == Staff:
			if person.assigned_office == room_name:
				print ("\n"+person.person.upper()+" is already assigned to "+room_name.upper()+"\n")
			else:
				for room in self.all_rooms:
					if room.room_name == room_name and type(room) == OfficeSpace:
						if self.is_room_available(room) == True:
							room.occupants.append(person)
							person.assigned_office = room.room_name
							if room not in self.allocated_rooms: self.allocated_rooms.append(room)
							print ("\n You have reallocated "+person.person.upper()+" to "+room.room_name.upper()+"\n")
						else:
							print ("\n"+room.room_name+" is full. \n")
					elif room.room_name == room_name and type(room) is not OfficeSpace:
						print("\n Staff cannot be assigned to living spaces. \n")
		elif type(person) == Fellow:
			if person.assigned_office == room_name:
				print ("\n"+person.person.upper()+" is already assigned to "+room_name.upper()+"\n")
			elif person.assigned_living == room_name:
				print ("\n"+person.person.upper()+" is already assigned to "+room_name.upper()+"\n")
			else:
				for room in self.all_rooms:
					if room.room_name == room_name:
						if self.is_room_available(room) == True:
							if type(room) == LivingSpace:
								person.assigned_living = room.room_name
								print ("\n You have reallocated "+person.person.upper()+" to "+room.room_name.upper()+"\n")
							elif type(room) == OfficeSpace:
								person.assigned_office = room.room_name
								print ("\n You have reallocated "+person.person.upper()+" to "+room.room_name.upper()+"\n")
							room.occupants.append(person)
							if room not in self.allocated_rooms: self.allocated_rooms.append(room)
						else:
							print ("\n"+room.room_name+" is full. \n")				
	
	def load_people_from_file(self, filename):
			with open("./models/"+filename, mode="r") as text:
				people_list = text.readlines()
				for people in people_list:
					person = people.split()
					person_name = person[0]+" "+person[1]
					role = person[2]
					if role == "STAFF":
						person_dict = {"person_name":person_name, "role":"staff"}
						self.create_person(person_dict)
					if role == "FELLOW":
						accomodation = person[3]
						person_dict = {"person_name":person_name, "role":"fellow", "wants_accomodation":accomodation}
						self.create_person(person_dict)

	def write_allocated_to_terminal(self):
		print ("\n Printing allocations to the terminal... \n")
		for room in self.all_rooms:
			text = "\n"+room.room_name.upper()+"\n"
			text = text + ("-"*40 + "\n")			
			if len(room.occupants) > 0:
				text = text + ", ".join([occupant.person.upper() for occupant in room.occupants])
			else:
				text = text + "\n No one has been allocated yet. \n"
			print (text)

	def write_allocated_to_file(self, filename):
		print ("\n Printing allocations to txt file... "+filename)
		with open(filename, mode="w", encoding='utf-8') as text:
			for room in self.allocated_rooms:
				if len(room.occupants) > 0:
					text.write(room.room_name.upper()+"\n")
					text.write("-"*40 +"\n")
					text.write(", ".join([occupant.person.upper() for occupant in room.occupants]))	
				else:
					text.write("No one has been allocated yet.")
			
	def write_unallocated_to_terminal(self):
		print ("\n Printing unallocated people to the terminal... \n")
		if len(self.unallocated_people) > 0:
			text = "\n Unallocated people:"+"\n"
			text = text + ("-"*40 + "\n")
			text = text + (", ".join([person.person.upper() for person in self.unallocated_people]))
		else: 
			text = text + "There are currently no unallocated people.\n"
		print (text)
			
	def write_unallocated_to_file(self, filename):
		print ("\n Printing unallocated people to txt file "+filename)
		with open(filename, mode="w", encoding='utf-8') as text:
			if len(self.unallocated_people) > 0:
				text.write("Unallocated people:"+"\n")
				text.write("-"*40 +"\n")
				text.write(", ".join([person.person.upper() for person in self.unallocated_people]))
			else:
				text.write("There are currently no unallocated people.")

	def print_room(self, room_name):
		for room in self.all_rooms:
			if room.room_name == room_name:
				if len(room.occupants) > 0:
					text = (room.room_name.upper() +"\n")
					text = text + ("-"*50 +"\n")
					text = text + (", ".join([occupant.person.upper() for occupant in room.occupants]))
				else:
					text = ("This room is empty. \n")	
				print (text)


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

			