import unittest
from app.room import Room
from app.person import Person

	# # Create a test for room type
	# def test_living_room_type(self):
	# 	room = Room()
	# 	room.room_type("living")
	# 	self.assertEqual(room.room_type, "living")
		

	# def test_office_room_capacity(self):
	# # An office has a max capacity of 4 people
	# 	self.oculus = self.utility.createRoom({"roomName":"Oculus", "roomType":"officeSpace", "roomCapacity": "6"})
	# 	self.assertTrue(self.oculus["roomType"], self.oculus["roomCapacity"] = "6")

	# def test_living_room_capacity(self):
	# # A living room has a max capacity of 6 people
	# 	self.ruby = self.utility.createRoom({"roomName":"Ruby", "roomType":"livingSpace", "roomCapacity": "4"})
	# 	self.assertTrue(self.ruby["roomType"], self.ruby["roomCapacity"] = "4")

	

	# # Staff can be assigned to offices only. 
	# # Fellows can be assigned to an office and a living space. 
	# def test_fellow_can_be_allocated_to_office_room(self):
	# 	self.oculus = self.utility.createRoom({"roomName":"Oculus", "roomType":"officeSpace"})
	# 	self.rehema = self.utility.createPerson({"firstName":"Rehema", "lastName":"Wachira", "role":"fellow"})
	# 	self.assignedRoom = self.utility.assignRoom(self.rehema, self.oculus)
	# 	self.assertTrue(self.assignedRoom["roomType"], "officeSpace")
	# 	# self.assertTrue(self.rehema["role"], self.assignedRoom["roomType"])

	# def test_fellow_can_be_allocated_to_living_room(self):
	# 	self.ruby = self.utility.createRoom({"roomName":"Ruby", "roomType":"livingSpace"})
	# 	self.rehema = self.utility.createPerson({"firstName":"Rehema", "lastName":"Wachira", "role":"fellow"})
	# 	self.assignedRoom = self.utility.assignRoom(self.rehema, self.ruby)
	# 	self.assertTrue(self.assignedRoom["roomType"], "livingSpace")

	# def test_staff_can_be_allocated_to_office_room(self):
	# 	self.oculus = self.utility.createRoom({"roomName":"Oculus", "roomType":"officeSpace"})
	# 	self.percila = self.utility.createPerson({"firstName":"Percila", "lastName":"Njira", "role":"staff"})
	# 	self.assignedRoom = self.utility.assignRoom(self.percila, self.oculus)
	# 	self.assertTrue(self.assignedRoom["roomType"], "officeSpace") 

	# def test_staff_cannot_be_allocated_to_living_room(self):
	# # Test that error is raised when staff is allocated a livingSpace room 
	# 	self.ruby = self.utility.createRoom({"roomName":"Ruby", "roomType":"livingSpace"})
	# 	self.percila = self.utility.createPerson({"firstName":"Percila", "lastName":"Njira", "role":"staff"})
	# 	self.assertRaises(self.utility.assignRoom(), self.percila, self.ruby)
		
	# def test_person_cannot_be_assigned_to_more_than_one_room(self):
	# # Each person can only be assigned to one office space/living room at a time.
	# 	self.oculus = self.utility.createRoom({"roomName":"Oculus", "roomType":"officeSpace"})
	# 	self.narnia = self.utility.createRoom({"roomName":"Narnia", "roomType":"officeSpace"})
	# 	self.rehema = self.utility.createPerson({"firstName":"Rehema", "lastName":"Wachira", "role":"fellow"})
	# 	self.assertRaises(self.utility.assignRoom(), self.rehema, self.oculus, self.narnia)
		
	# def test_if_room_raises_alert_when_room_is_full(self):
	# # Create a room occupancy counter. 
	# 	self.oculus = self.utility.createRoom({"roomName":"Oculus", "roomType":"officeSpace", "capacity": "6"})
	# 	self.roomCounter = self.utility.getRoomOccupancy(self.oculus)
	# 	self.rehema = self.utility.createPerson({"firstName":"Rehema", "lastName":"Wachira", "role":"fellow"})
	# 	self.brian = self.utility.createPerson({"firstName":"Brian", "lastName":"Kimokoti", "role":"fellow"})
	# 	self.sam = self.utility.createPerson({"firstName":"Sam", "lastName":"Gaamura", "role":"fellow"})
	#  	self.whitney = self.utility.createPerson({"firstName":"Whitney", "lastName":"Ruoro", "role":"fellow"})
	#  	self.joseph = self.utility.createPerson({"firstName":"Joseph", "lastName":"Muli", "role":"fellow"})
	#  	self.ruth = self.utility.createPerson({"firstName":"Ruth", "lastName":"Ogendi", "role":"fellow"})
	# 	self.assignedRoom = self.utility.assignRoom(self.rehema, self.oculus)
	# 	self.assignedRoom = self.utility.assignRoom(self.brian, self.oculus)
	# 	self.assignedRoom = self.utility.assignRoom(self.sam, self.oculus)
	# 	self.assignedRoom = self.utility.assignRoom(self.whitney, self.oculus)
	# 	self.assignedRoom = self.utility.assignRoom(self.joseph, self.oculus)
	# 	self.assignedRoom = self.utility.assignRoom(self.ruth, self.oculus)
	# 	self.roomCounter = self.utility.getRoomOccupancy(self.oculus)
	# 	self.assertEqual(self.oculus["capacity"], self.roomCounter, msg="This room is full")


	
	# # # def test_stop_allocations_for_full_rooms(self):
	# # # Prevent additional people from being assignged to a room that is full.

	# # # def test_alert_if_living_room_is_full(self):
	# # # 	pass

	# def test_create_list_of_all_current_occupants_in_office_room(self):
	# 	# test assigning someone to a room then output a list with
	# 	# them in it. 
		


	# # def test_create_list_of_all_current_occupants_in_living_room(self):
	# 	pass

	# def test_create_list_of_all_unallocated_people(self):
	# 	pass

	# def test_create_list_of_all_unallocated_rooms(self):
	# 	pass

	# def test_room_reallocation(self):
	# # Should be able to delete a person from their current room and
	# # reallocate them to a different room
	# 	pass

	# Test Amity keeps record of all rooms created???

if __name__ == '__main__':
	unittest.main()