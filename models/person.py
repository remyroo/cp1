class Person(object):
	def __init__(self, person):
		self.person = person
		self.assigned_office = ""
	
	def __repr__(self):
		return "%s" % (self.person)

	@property
	def role(self):
		return self.__class__.__name__

class Staff(Person):	
	pass

class Fellow(Person):
	def __init__(self, person):
		super(Fellow, self).__init__(person)
		self.accomodation = ""
		self.assigned_living = ""



