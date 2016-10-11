class Room(object):
	def __init__(self, room_name):
		self.room_name = room_name
		self.occupants = []
	
	def __repr__(self):
		return "%s" % (self.room_name)

	@property
	def room_type(self):
		return self.__class__.__name__

class OfficeSpace(Room):
	capacity = 6	

class LivingSpace(Room):
	capacity = 4

