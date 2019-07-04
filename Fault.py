class Fault:
	def __init__ (self, name, faultRelay = False, shortRelay = False, resistRelay = False):
		self.name = name
		self.faultRelay = faultRelay
		self.shortRelay = shortRelay
		self.resistRelay = resistRelay
			 