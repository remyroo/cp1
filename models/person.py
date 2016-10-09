class Person(object):
	def __init__(self, person):
		self.person = person
		self.assigned_office = ""
	
	def __repr__(self):
		return "%s" % self.person

	@property
	def role(self):
		return self.__class__.__name__

class Staff(Person):	
	pass

class Fellow(Person):
	assigned_living = ""
	pass



